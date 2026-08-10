---
partOf: "[[automation framework]]"
facet of: "[[requirements analysis]]"
subclass of: "[[possibility]]"
wikidata entity id: Q7430721
broader: "[[application development]]"
inferred:skos:ancestor:
  - "[[Process]]"
  - "[[application development]]"
---
In [computing](https://en.wikipedia.org/wiki/Computing "Computing"), a **scenario** (, ; [loaned](https://en.wikipedia.org/wiki/Loanword "Loanword") from [Italian](https://en.wikipedia.org/wiki/Italian_language "Italian language") _scenario_ (pronounced [[ʃeˈnaːrjo]](https://en.wikipedia.org/wiki/Help:IPA/Italian "Help:IPA/Italian")), from [Latin](https://en.wikipedia.org/wiki/Latin_language "Latin language") _scena_ 'scene'[[1]](#cite_note-1)) is a narrative of foreseeable [interactions](https://en.wikipedia.org/wiki/Human%E2%80%93computer_interaction "Human–computer interaction") of user roles (known in the [Unified Modeling Language](https://en.wikipedia.org/wiki/Unified_Modeling_Language "Unified Modeling Language") as '[actors](https://en.wikipedia.org/wiki/Actor_\(UML\) "Actor (UML)")') and the technical system, which usually includes [computer hardware](https://en.wikipedia.org/wiki/Computer_hardware "Computer hardware") and [software](https://en.wikipedia.org/wiki/Software "Software").

A scenario has a [goal](https://en.wikipedia.org/wiki/Goal_modeling "Goal modeling"), which is usually functional. A scenario describes one way that a system is used, or is envisaged to be used, in the context of an activity in a defined time-frame. The time-frame for a scenario could be (for example) a single transaction; a business operation; a day or other period; or the whole [operational life](https://en.wikipedia.org/wiki/Operational_life "Operational life") of a system. Similarly the scope of a scenario could be (for example) a single system or a piece of equipment; an equipped team or a department; or an entire organization.

Scenarios are frequently used as part of the system development process. They are typically produced by usability or [marketing](https://en.wikipedia.org/wiki/Marketing "Marketing") specialists, often working in concert with end users and developers. Scenarios are written in plain language, with minimal technical details, so that [stakeholders](https://en.wikipedia.org/wiki/Stakeholder_theory "Stakeholder theory") (designers, usability specialists, programmers, engineers, managers, marketing specialists, etc.) can have a common ground to focus their discussions.

Increasingly, scenarios are used directly to define the wanted behaviour of software: replacing or supplementing traditional [functional requirements](https://en.wikipedia.org/wiki/Functional_requirement "Functional requirement"). Scenarios are often defined in [use cases](https://en.wikipedia.org/wiki/Use_case "Use case"), which document alternative and overlapping ways of reaching a goal.[[2]](#cite_note-2)

## Types of scenario in system development

[[edit](https://en.wikipedia.org/w/index.php?title=Scenario_\(computing\)&action=edit&section=1 "Edit section: Types of scenario in system development")]

Many types of scenario are in use in system development. Alexander and Maiden[[3]](#cite_note-AlexMaid-3) list the following types:

- **[Story](https://en.wikipedia.org/wiki/Narrative "Narrative")**: "a narrated description of a causally connected sequence of events, or of actions taken".[[3]](#cite_note-AlexMaid-3) : 8–10  Brief [User stories](https://en.wikipedia.org/wiki/User_story "User story") are written in the [Agile](https://en.wikipedia.org/wiki/Agile_software_development "Agile software development") style of software development.[[4]](#cite_note-Cohn,_2004-4)
- **Situation, [Alternative World](https://en.wikipedia.org/wiki/Scenario_analysis "Scenario analysis")**: "a projected future situation or snapshot". This meaning is common in planning, but less usual in software development.[[3]](#cite_note-AlexMaid-3) : 10 
- **[Simulation](https://en.wikipedia.org/wiki/Simulation "Simulation")**: use of models to explore and animate 'Stories' or 'Situations', to "give precise answers about whether such a scenario could be realized with any plausible design" or "to evaluate the implications of alternative possible worlds or situations".[[3]](#cite_note-AlexMaid-3) : 10–11 
- **[Storyboard](https://en.wikipedia.org/wiki/Storyboard "Storyboard")**: a drawing, or a sequence of drawings, used to describe a user interface or to tell a story. This meaning is common in [Human–computer interaction](https://en.wikipedia.org/wiki/Human%E2%80%93computer_interaction "Human–computer interaction") to define what a user will see on a screen.[[3]](#cite_note-AlexMaid-3) : 12 
- **Sequence**: a list of interactive steps taken by human or machine agents playing system roles. The many forms of scenario written as sequences of steps include Operational Scenarios, Concepts of Operations, and Test Cases.[[3]](#cite_note-AlexMaid-3) : 12–14 
- **Structure**: any more elaborately-structured representation of a scenario, including [Flowcharts](https://en.wikipedia.org/wiki/Flowchart "Flowchart"), [UML](https://en.wikipedia.org/wiki/Unified_Modelling_Language "Unified Modelling Language")/ITU 'Sequence Charts', and especially in software development [Use cases](https://en.wikipedia.org/wiki/Use_case "Use case").[[3]](#cite_note-AlexMaid-3) : 14–17 

Negative scenarios or [misuse cases](https://en.wikipedia.org/wiki/Misuse_case "Misuse case") may be written to indicate likely threats which should be countered to ensure that systems have sufficient [security](https://en.wikipedia.org/wiki/Security "Security"), [safety](https://en.wikipedia.org/wiki/Safety "Safety"), and [reliability](https://en.wikipedia.org/wiki/Reliability_engineering "Reliability engineering"). These help to discover [non-functional requirements](https://en.wikipedia.org/wiki/Non-functional_requirements "Non-functional requirements").[[5]](#cite_note-Negative-5)

## Uses in system development

[[edit](https://en.wikipedia.org/w/index.php?title=Scenario_\(computing\)&action=edit&section=2 "Edit section: Uses in system development")]

Scenarios have numerous possible applications in system development. Carroll (1995) lists 10 different "roles of scenarios in the system development lifecycle":[[6]](#cite_note-Carroll1995-6)

1. **[Requirements analysis](https://en.wikipedia.org/wiki/Requirements_analysis "Requirements analysis")**: scenarios describe the "state-of-the-art" (often called "as-is"); acted scenarios help to discover requirements as analysts "stage a simulated work situation".
2. **[User-designer communication](https://en.wikipedia.org/wiki/Requirements_elicitation "Requirements elicitation")**: users contribute scenarios important to them, or situations they want to experience or avoid.[[6]](#cite_note-Carroll1995-6)
3. **[Design rationale](https://en.wikipedia.org/wiki/Design_rationale "Design rationale")**: rationale can explain design "with respect to particular scenarios of user interaction".[[6]](#cite_note-Carroll1995-6)
4. **[Envisionment](https://en.wikipedia.org/wiki/Mockup "Mockup")**: scenarios "can be a medium for working out what a system being designed should look like and do." In this role, scenarios can be "graphical mockups such as storyboards or video-based simulations", and may form early [prototypes](https://en.wikipedia.org/wiki/Prototype "Prototype") of the system under design.[[6]](#cite_note-Carroll1995-6)
5. **[Software design](https://en.wikipedia.org/wiki/Software_design "Software design")**: "scenarios can be analyzed to identify the central problem domain objects" needed; the same scenarios can be developed to describe the objects' state, behavior and interactions.[[6]](#cite_note-Carroll1995-6)
6. **[Implementation](https://en.wikipedia.org/wiki/Implementation "Implementation")**: software can be built one scenario at a time, helping "to keep developers focused" and "producing code that is more generally useful".[[6]](#cite_note-Carroll1995-6)
7. **[Documentation](https://en.wikipedia.org/wiki/Software_documentation "Software documentation") and [Training](https://en.wikipedia.org/wiki/Training "Training")**: "scenarios of interaction that are meaningful to the users" can bridge the gap between the system as built "and the tasks that users want to accomplish using it".[[6]](#cite_note-Carroll1995-6)
8. **[Evaluation and testing](https://en.wikipedia.org/wiki/Software_testing "Software testing")**: since "a system must be evaluated against the specific user tasks it is intended to support", scenarios are ideal for evaluation.[[6]](#cite_note-Carroll1995-6)
9. **[Abstraction](https://en.wikipedia.org/wiki/Abstraction "Abstraction")**: general rules that apply across different tasks (or systems) can be identified by comparing scenarios.[[6]](#cite_note-Carroll1995-6)
10. **[Team building](https://en.wikipedia.org/wiki/Team_building "Team building")**: "a set of touchstone stories is an important cohesive element in any social system".[[6]](#cite_note-Carroll1995-6)

## In differing styles of system development

[[edit](https://en.wikipedia.org/w/index.php?title=Scenario_\(computing\)&action=edit&section=3 "Edit section: In differing styles of system development")]

The choice of scenario representation varies widely with style of development, which is related to the industrial context.

|   |   |   |   |
|---|---|---|---|
Scenarios in differing project contexts
|Project context|Example|Scenario style|Development style|
|Large military project|Fighter aircraft|[Operational View](https://en.wikipedia.org/wiki/Operational_View "Operational View"), [Concept of operations](https://en.wikipedia.org/wiki/Concept_of_operations "Concept of operations")|Staged life-cycles, thorough documentation (see [DoDAF](https://en.wikipedia.org/wiki/Department_of_Defense_Architecture_Framework "Department of Defense Architecture Framework"))|
|Combined Hardware/Software product|Car|[Use case](https://en.wikipedia.org/wiki/Use_case "Use case")[[7]](#cite_note-7)|[RUP](https://en.wikipedia.org/wiki/IBM_Rational_Unified_Process "IBM Rational Unified Process")|
|Business software|Mobile phone application|[User story](https://en.wikipedia.org/wiki/User_story "User story")[[4]](#cite_note-Cohn,_2004-4)|[Agile software development](https://en.wikipedia.org/wiki/Agile_software_development "Agile software development")|

- [Happy path](https://en.wikipedia.org/wiki/Happy_path "Happy path")
- [Scenario testing](https://en.wikipedia.org/wiki/Scenario_testing "Scenario testing")
- [Strategic assumptions](https://en.wikipedia.org/wiki/Strategic_assumptions "Strategic assumptions")
- [Computer supported brainstorming](https://en.wikipedia.org/wiki/Computer_supported_brainstorming "Computer supported brainstorming")

1. **[^](#cite_ref-1 "Jump up")** [etymonline.com](https://www.etymonline.com/search?q=scenario)
2. **[^](#cite_ref-2 "Jump up")** Alexander and Beus-Dukic, 2009. Page 120
3. ^ [Jump up to: _**a**_](#cite_ref-AlexMaid_3-0) [_**b**_](#cite_ref-AlexMaid_3-1) [_**c**_](#cite_ref-AlexMaid_3-2) [_**d**_](#cite_ref-AlexMaid_3-3) [_**e**_](#cite_ref-AlexMaid_3-4) [_**f**_](#cite_ref-AlexMaid_3-5) [_**g**_](#cite_ref-AlexMaid_3-6) Alexander and Maiden, 2004. Chapter 1.
4. ^ [Jump up to: _**a**_](#cite_ref-Cohn,_2004_4-0) [_**b**_](#cite_ref-Cohn,_2004_4-1) Cohn, 2004.
5. **[^](#cite_ref-Negative_5-0 "Jump up")** Alexander and Maiden, 2004. Chapter 7.
6. ^ [Jump up to: _**a**_](#cite_ref-Carroll1995_6-0) [_**b**_](#cite_ref-Carroll1995_6-1) [_**c**_](#cite_ref-Carroll1995_6-2) [_**d**_](#cite_ref-Carroll1995_6-3) [_**e**_](#cite_ref-Carroll1995_6-4) [_**f**_](#cite_ref-Carroll1995_6-5) [_**g**_](#cite_ref-Carroll1995_6-6) [_**h**_](#cite_ref-Carroll1995_6-7) [_**i**_](#cite_ref-Carroll1995_6-8) [_**j**_](#cite_ref-Carroll1995_6-9) Carroll, 1995. Pages 7-8
7. **[^](#cite_ref-7 "Jump up")** Cockburn, 2011.

- Alexander, Ian and Beus-Dukic, Ljerka. _Discovering Requirements: How to Specify Products and Services_. Wiley, 2009.
- Alexander, Ian F. and Maiden, Neil. _Scenarios, Stories, Use Cases_. Wiley, 2004.
- Carroll, John M. (ed) _Making Use: Scenario-based Design of Human-Computer Interactions_. MIT Press, 2000.
- Carroll, John M. (ed) _Scenario-Based Design: Envisioning Work and Technology in System Development_. Wiley, 1995.
- Cockburn, Alistair. _Writing Effective Use Cases_. Addison-Wesley, 2001.
- Cohn, Mike. _User Stories Applied: for Agile Software Development_. Addison-Wesley, 2004.
- Fowler, Martin. _UML Distilled_. 3rd Edition. Addison-Wesley, 2004.

- [Notes on Design Practice: Stories and Prototypes as Catalysts for Communication.](http://tomeri.org/Stories.html) by Thomas Erickson, in Carroll, 1995.