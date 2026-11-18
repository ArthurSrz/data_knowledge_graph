
# Does [[knowledge]] drives [[token]] efficiency ? 


Today we set out to prove that [[knowledge]] layers help reduce [[token]] consumption **and save users' time**. Why would we want to prove that ? 

First, because it is a common intuition that the more you know, the less you speak/generate. Or, as we say in french about culture : 

> [!quote]
> La culture, c'est comme la confiture, moins tu en as, plus tu l'étales. (*Culture is like jam: the less you have, the more you spread it.*)

And [[token]] jam became quite expansive these days ! So proving that [[knowledge]] layers help reduce [[token]] consumption would confirm both the saying and the intuition. 

Second, because trying to prove that is a way to stress-[[test]] the hypothesis that [[knowledge]] reduces the natural semantic dispersion of [[large language model]]. For it is reasonable enough to assume that the sparser a [[model]]'s [[output]], semantically speaking, the more iterations are required to [[reach]] a given [[outcome]]. And the more iterations, the more tokens you consume. 

Third, and most important , if [[knowledge]] does drive [[token]] efficiency, because it gets you semantically deep and precise [[output]] faster, that would confirm (as [Alban Leveau-Vallier has argued](https://hyper.hypotheses.org/171)) , that traveling through a [[latent space]] is the right way to think about [[Generation]].


> [!summary] Interlude
> If we prove that [[knowledge]] drives [[token]] efficiency, it would echo the French saying that culture, like jam, gets spread thinner the less you have. The logic: without [[knowledge]] LLM outputs are semantically sparse, so you need more iterations and more tokens to [[reach]] [[precision]]. Confirming this would also support Alban Leveau-Vallier's view of [[generation]] as travel through a [[latent space]] where [[knowledge]] is like a map that shows a faster [[path]] toward destination

Now, let's get down to the hard part : designing an experiment simple enough and good enough to prove it.

## Designing a [[token]]-efficiency experiment

The hardest part is usually agreeing on an *end state*, by which I mean here : at chat point do we decde it is no longer necessary to consume tokens to [[reach]] the goal ? Once that's settled, we can [[test]] different solutions (some with [[knowledge]] layers, some without, some with different types of [[knowledge]] layers and so on). 

Funnily enough, I'd argue that a finished solution is **one that resembles an original human-made solution so closely that we can no longer distinguish which is which**. The idea isn't mine, it is Turing's: a finished solution is one that passes the [[Turing test]]. Turing held that intelligence itself can be measured this way, by whether the imitation holds up. 

In other words, you know you should stop spending tokens once you can no longer distinguish the generated [[output]] from the human original.

So here is the objective, restated : 

> Do [[knowledge]] layers help generated ouput pass the [[turing test]] faster ? 

> [!summary] Interlude 
> Designing the experiment first requires agreeing on an end state, i.e the point at which consuming more tokens is no longer necessary to [[reach]] the goal. The proposed criterion, borrowed from Turing, is indistinguishability: the [[output]] is done once it resembles a human-made original so closely that you can't tell which is which. This reframes the whole question as: do [[knowledge]] layers help generated [[output]] pass the [[turing test]] faster?

The simplest end state to agree on is a slide. Why a slide ? Because a slide is simple, and it demands both semantic and visual [[precision]].

So I'll take the human-slide below, and that will be our end state. 

![[good_visually.png]]

### Scoring the generated slide against the original

As I said, if the generated slide passes the Turing tests, the end state has been reached and we should stop spending tokens. But the [[Turing test]] is unavoidably subjective : some people will be unsure, others will guess wrong, others will spot the AI instantly. 

So we need more than a [[turing test]]. We need metrics. I propose three: 

1. **Structure [[metric]]** : how many **structural elements** in the generated [[output]] match the original ? 
2. **Content [[metric]]** : what is the [[distance]] between the generated word sequences and the original ones ? 
3. **Visual [[metric]]** : LLM-as-a judge: the [[model]] reports which [[differences]] it finds between the generated slide and the original.


In the slide above we see : 
* 5 structure elements (1 title and 4 boxes)
* 10 word sequences 
* 1 visual [[design]]: relatively small title, generous white space and a distinctive color palette

> [!summary] Interlude
> The chosen end state is a human-made slide, since a slide is simple yet demands both semantic and visual [[precision]]. Because the [[turing test]] alone is too subjective, quality is measured with three metrics: a structure [[metric]] (how many structural elements match the original), a content [[metric]] (the [[distance]] between generated and original word sequences), and a visual [[metric]] (an LLM-as-judge comparing the two slides). The reference slide has 5 structure elements (1 title, 4 boxes), 10 word sequences, and a distinct visual [[design]] featuring a small title, generous spacing, and a clear color palette.

All in all, the end state is reached once : 

* The structure matches perfectly
* The content [[distance]] is near zero
* The LLM judge spots no visual difference

### Counting what each harness consumes

That's the easy part. I ran 4 different harness, each with its native LLM attached: 
* [[Claude]] Cowork (with Sonnet 5)
* Google AI Studio (with Gemini and Nano Banana 2)
* [[clarifeye]] tasks
* [[Claude]] Cowork + [[clarifeye]]

And for each one I measured three things: the number of tokens consumed, the percentage of a usage [[session]] it burned, and the time spent generating


##### Harness 1 : [[claude cowork]] 

It took **64 minutes** to [[reach]] a slide that might pass the [[turing test]], and consumed 6% of my [[session]] allowance. Here is the [[output]]:

![[claude-slides.pdf]]

The interesting part: I hit a plateau after the fourth iteration, past which each new prompt risked taking me further from the [[target]] rather than closer. Note the sequence: I started with prompting alone, then supplied template files, then made minor refinements.

To put numbers on what I mean by "might pass the [[Turing test]]" : 

![[results-it1-convergence-experimentation.png]]

* 4 identical sections out of 5 
* Content is 28% identical semantically, 21,5% literally
* 2 major visual [[differences]] : title hierarchy and spacing. 

> [!summary] Interlude
> Prompting alone gets you close on structure but stalls on everything else. After four iterations [[claude cowork]] hit a plateau—more [[prompts]] started pushing the slide away from the [[target]] rather than toward it. The result: sections mostly matched, but content overlap stayed low (28% semantic, 21.5% literal) and two visual gaps persisted in title hierarchy and spacing.

##### Harness 2 : Google AI Studio

It took 20 minutes to [[reach]] a slide that might pass the Turing Tests, and consumed 21k tokens at a cost 0,5€ with Nano Banana 2. Here is the [[output]]: 
![[slide_gemini.jpg]]

Worth noting: it exceeded the [[token]] window mid-run and I had to switch to another [[model]] to finish.

The numbers

![[score_gemini.png]]

* Structure matches exactly
* content is 47% identical semantically speaking and 38,5% literally speaking 
* 1 major visual difference (letter spacing)

> [!summary] Interlude
> Adding image [[generation]] to the mix moved the needle. Google AI Studio got there in a third of the time, matched the structure exactly, and roughly doubled the content overlap (47% semantic, 38.5% literal), leaving just one visual gap in letter spacing. The catch: it blew past the [[token]] window mid-run and forced a [[model]] switch to finish.
##### Harness 3: [[Clarifeye]] tasks

25 minutes and €12 later, consumed 2,2 million [[token]] in and 24k [[output]] tokens. Here is the [[output]]:

![[clarifeye_tasks_png.png]]

The numbers: 
![[clarifeye_tasks.png]]
Every block matches, but content overlap sits at 15% semantically.

> [!summary] Interlude
> [[clarifeye]] in build mode nailed the structure completely (every block matched) but at a steep price: 25 minutes, 12 euros, and 2.2 million tokens in. Structure isn't the bottleneck anymore; content is. The score plateaus not because the layout is wrong, but because the words still drift from the original (15% semantic overlap), which is exactly where [[knowledge]] should start earning its keep.

##### Harness 4: [[Claude]] + [[clarifeye]] (use mode + MCP)

10 minutes, 2% of [[Claude]] usage window, 0 euros CCU. 

![[clarifeye_mcp.pdf]]



The numbers: 

![[full_results_mcp.png]]

We got an impressive core on the content driven by high semantic similarity 

![[details_clarifeye_MCP.png]]

> [!summary] Interlude 
> This is the run where [[knowledge]] pays off. [[Claude]] plus [[clarifeye]] in use mode (via MCP) reached the [[target]] in 10 minutes, on 2% of a usage window, at zero marginal cost—and the content jumped to 89% semantic similarity. Structure held, and the words finally converged on the original instead of drifting: the [[knowledge]] [[layer]], not more prompting, is what closed the gap.

## What the numbers say 

I set out to [[test]] one claim: that [[knowledge]] layers help generated [[output]] pass the [[Turing test]] faster, and with fewer tokens. **Across four harnesses, the [[pattern]] is clear.**

Raw prompting ([[Claude Cowork]]) plateaus early: good structure, but content stalls at 28%, and the run burns through the most [[session]] budget for the weakest result. Adding image [[generation]] (Google AI Studio) roughly doubles content fidelity and sharpens the visuals, but overflows the [[token]] window. Throwing compute at the problem through [[Clarifeye]] build mode nails structure perfectly, yet at 2.2 million tokens and €12 it still leaves content at 15%. An evidence that more tokens alone don't close the semantic gap.

But the [[knowledge]] [[layer]] does ! [[Claude]] plus [[Clarifeye]] in use mode reached the [[target]] in 10 minutes, on 2% of a usage window, at zero marginal cost **and content fidelity jumped to 89%.** Same [[model]] family, a fraction of the resources, and the variable that changed was access to structured [[knowledge]].

This is what the opening hypothesis predicted: [[knowledge]] reduces the semantic dispersion of the [[model]]'s [[output]], so fewer iterations are needed to converge on a precise result. **And fewer iterations mean fewer tokens.** 

Culture, like jam, spreads thinner the less you have. Or, in Leveau-Vallier's terms: if [[generation]] is travel through a [[latent space]], [[knowledge]] is the map that shows the shortest [[path]] to the destination.

The cheapest, fastest run wasn't the one with the most compute. It was the one that knew where it was going.