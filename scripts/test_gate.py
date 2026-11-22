#!/usr/bin/env python3
"""Tests for `reason.py gate`. Run: .venv-gate/bin/python scripts/test_gate.py

Unit: each violation kind, positive (injected error is caught) and negative
(a legitimate shape is not). Integration: process owner on the real graph.
"""
import contextlib
import io
import tempfile
import unittest
from pathlib import Path

import reason

BASE = {  # tiny ontology: two disjoint top classes
    "c1": "---\ndisjoint with: \"[[c2]]\"\n---\n",
    "c2": "---\ndisjoint with: \"[[c1]]\"\n---\n",
}


def note(**rels):
    lines = [f'{k.replace("_", " ")}: "[[{v}]]"' if isinstance(v, str)
             else f'{k.replace("_", " ")}:\n' + "\n".join(f'  - "[[{t}]]"' for t in v)
             for k, v in rels.items()]
    return "---\n" + "\n".join(lines) + "\n---\n"


def kinds(overlay, base=None):
    with contextlib.redirect_stdout(io.StringIO()):
        return {k for k, _, _ in reason.gate(overlay, base)[0]}


class Unit(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.real = reason.GRAPH_DIR
        reason.GRAPH_DIR = Path(self.tmp.name)
        for name, text in BASE.items():
            (reason.GRAPH_DIR / f"{name}.md").write_text(text)

    def tearDown(self):
        reason.GRAPH_DIR = self.real
        self.tmp.cleanup()

    def test_cycle(self):
        self.assertIn("in_cycle", kinds({"a": note(broader="b"), "b": note(broader="a")}))
        self.assertEqual(set(), kinds({"a": note(broader="b"), "b": note(broader="c1")}))

    def test_s27(self):
        self.assertIn("s27_violation", kinds({"a": note(broader="b", **{"skos:related": "b"}), "b": ""}))
        self.assertEqual(set(), kinds({"a": note(broader="b", **{"skos:related": "c2"}), "b": ""}))

    def test_opposites(self):
        self.assertIn("conflict", kinds({"a": note(oppositeOf="b", **{"skos:related": "b"}), "b": ""}))
        self.assertEqual(set(), kinds({"a": note(oppositeOf="b"), "b": ""}))

    def test_disjoint(self):
        self.assertIn("disjoint_violation", kinds({"x": note(subclass_of=["c1", "c2"])}))
        self.assertEqual(set(), kinds({"x": note(subclass_of="c1")}))

    def test_part_cycle(self):
        self.assertIn("part_cycle", kinds({"a": note(part_of="b"), "b": note(part_of="a")}))
        self.assertEqual(set(), kinds({"a": note(part_of="b"), "b": ""}))

    def test_cross_level(self):
        # an individual: instance of c1, subclass of c2
        self.assertIn("cross_violation", kinds({"x": note(instance_of="c1", subclass_of="c2")}))
        # a class (has a subclass) may also be an instance of a metaclass
        self.assertEqual(set(), kinds({"k": note(instance_of="c1", subclass_of="c2"),
                                       "k2": note(subclass_of="k")}))

    def test_only_new_violations(self):
        (reason.GRAPH_DIR / "a.md").write_text(note(broader="b"))
        (reason.GRAPH_DIR / "b.md").write_text(note(broader="a"))  # pre-existing cycle
        self.assertEqual(set(), kinds({"z": note(broader="c1")}))

    def test_base_overlay(self):
        (reason.GRAPH_DIR / "x.md").write_text(note(subclass_of=["c1", "c2"]))
        self.assertIn("disjoint_violation", kinds({}, base={"x": None}))  # x is new vs base


class Integration(unittest.TestCase):
    def test_process_owner(self):
        good = (reason.GRAPH_DIR / "process owner.md").read_text()
        bad = good.replace('subclass of: "[[person]]"\naccountable for: "[[business process]]"',
                           'subclass of:\n  - "[[person]]"\n  - "[[business process]]"')
        self.assertNotEqual(good, bad)
        self.assertIn("disjoint_violation", kinds({"process owner": bad}))
        self.assertEqual(set(), kinds({"process owner": good}))


if __name__ == "__main__":
    unittest.main()
