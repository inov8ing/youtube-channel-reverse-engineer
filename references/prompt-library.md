# Prompt Library for the Channel Blueprint

Use these prompts only after gathering evidence. Replace generic placeholders with specific source-backed findings; don't ask an LLM to invent proof.

## 1. Evidence-to-insight classifier

```text
You are an evidence auditor. Analyze only the supplied public-channel notes and cited sources.
For each proposed insight, output:
- Claim
- Classification: OBSERVED FACT / CALCULATION / INTERPRETATION / HYPOTHESIS / UNKNOWN
- Supporting evidence and exact source links
- What the evidence does not establish
- Alternative explanations
- Confidence and why
- A test the creator can run on their own channel
Do not infer impressions, CTR, retention, traffic sources, audience demographics, watch time, monetization, or revenue from public view counts. Do not state algorithm causality as fact. Identify unsupported claims and rewrite or remove them.
```

## 2. Topic opportunity research

```text
Act as a research editor and YouTube topic strategist. Channel promise: [PROMISE]. Audience: [AUDIENCE]. Reference patterns observed: [CITED OBSERVATIONS]. Available production resources: [RESOURCES].
Research current demand signals using public search results, relevant primary sources, official records, current conversations, and repeated audience questions where accessible. For every evidence-based claim, cite the source and date. Separate observed demand from interpretation. Never invent keyword search volume or trend growth.
Generate [N] distinct video ideas. Each idea must state: audience question, angle, evidence of demand, timeliness, differentiation, proof needed, visual feasibility, title directions, thumbnail concept, expected effort, rights/fact risks, and a falsifiable performance hypothesis. Reject ideas that only copy a competitor's exact subject/title or that lack a useful viewer payoff.
```

## 3. Long-form educational/explainer script

```text
Write an original [LENGTH]-minute [LANGUAGE] YouTube script for [AUDIENCE]. The video promise is [PROMISE] and the approved evidence pack is [SOURCES/FACTS].
Structure:
1. Start with the viewer's question, surprising evidence, result, or concrete stakes—no generic greeting.
2. State what the video will actually deliver and why the viewer should care.
3. Build an ordered sequence of useful explanations/demonstrations; each section must add a new fact, example, visual proof, or decision.
4. Use open questions only when they are answered later; no fake cliffhangers.
5. Surface material caveats and counterarguments.
6. Resolve the core promise before the CTA.
7. End with one relevant next step or related video—not a generic demand to subscribe.
Add a beat sheet with timestamp ranges, narration, visual proof, on-screen text, sound/edit notes, and source references. Cite factual claims in production notes. Do not invent quotations, statistics, personal experiences, or source attributions. Do not imitate the reference creator's wording or signature voice.
```

## 4. Short-form script

```text
Create an original [15–180]-second YouTube Short for [AUDIENCE] about [TOPIC], using [VERIFIED FACTS/EXPERIENCE]. Begin on the most visually clear action, result, question, or contradiction. Make the premise understandable without a long setup. Use short, natural lines and a coherent visual change for each beat. Deliver the promised payoff before the ending. Do not add filler, fake urgency, or an unfulfilled cliffhanger. If it loops, make the loop feel intentional without obscuring the point. Return: 3 hooks, the selected script, beat-by-beat visual plan, caption plan, audio notes, asset sources, and the single strongest viewer payoff. Don't copy a competitor's script or creator persona.
```

## 5. Beat-by-beat visual production plan

```text
Turn this approved script into a practical production plan: [SCRIPT].
For each beat, specify time range, narration/dialogue, viewer purpose, exact visual evidence needed, shot type/framing, movement, graphic/text, transition, sound/music, caption needs, asset type, asset source/license, and edit notes. Prefer original footage/screen recording first; then use appropriately licensed stock or public-domain media; use generated imagery/video only when suitable and clearly tracked. Maintain subject/style continuity, but don't replicate a competitor's exact frames, thumbnail, logo, proprietary assets, or the appearance/voice of a real creator. Mark any missing proof asset that could make the script misleading.
```

## 6. Thumbnail concept generator

```text
Analyze these observations about the reference channel's thumbnails: [OBSERVATIONS]. Do not copy any specific thumbnail. For this original video promise [PROMISE] and title [TITLE], create 3 visually distinct thumbnail concepts. Each must communicate one focal idea, remain readable at mobile size, use a clear subject/background separation, and complement rather than repeat the title. Specify composition, focal object/person, expression/action if appropriate, contrast, background, optional short text, color relationships, crop, and why the concept is truthful to the actual video. Give a generation prompt for an original image; no copied logos, exact layouts, creator likeness, or misleading result.
```

## 7. Title/thumbnail pairing critic

```text
Critique the following title/thumbnail pairs for an original video. Video summary and actual payoff: [SUMMARY]. Audience: [AUDIENCE]. Pairs: [OPTIONS].
Judge each on clarity, audience fit, curiosity without deception, specificity, mobile legibility, differentiation, evidence of the promise inside the video, and fit to Search or Browse intent. Identify redundancy between title and thumbnail. Return a short rationale and select the most promising variants to test. Do not claim a predicted CTR or view count.
```

## 8. SEO and upload QA

```text
Audit this YouTube upload package against the real video contents and current official YouTube guidance: [TITLE, DESCRIPTION, CHAPTERS, CAPTIONS, PLAYLIST, TAGS, HASHTAGS, THUMBNAIL SUMMARY, AUDIENCE SETTING, AI/RIGHTS NOTES].
Check accuracy, promise alignment, search-intent clarity, readability, useful chapters/links, metadata stuffing, misleading claims, caption quality, asset licensing, relevant policy/disclosure issues, and whether every title/thumbnail claim is supported by the video. Explain that tags play a limited role and do not promise ranking. Cite current official sources for platform-rule claims. Return corrected metadata and a final pass/fail checklist.
```

## 9. Post-publication diagnosis using the user's Analytics

```text
Analyze the supplied YouTube Studio data for my own channel only: [TIME WINDOW, FORMAT, DATA].
First confirm metric definitions, traffic-source segments, sample size, and comparisons. Separate factual observations from causal explanations. Diagnose possible bottlenecks in topic demand, packaging, opening, retention, payoff, audience fit, and follow-on viewing. Do not overreact to small samples or compare Shorts with long-form as if their metrics were interchangeable. Recommend at most 3 next experiments, each with a hypothesis, one main change, primary metric, diagnostic metric, review window, and decision rule. Explain uncertainty. Do not promise results.
```

## 10. Originality and rights review

```text
Review this planned video against its reference-channel inspiration: [REFERENCE NOTES], and the new concept/script/visuals: [DRAFT].
Identify any copied expression or identity signals: close paraphrase of script, distinctive catchphrase, exact thumbnail composition, reused footage/music, copied logo/branding, creator likeness/voice, or misleading association. Separate broad genre conventions from specific protected expression. Suggest precise changes that preserve the strategic lesson while making the work original. Check current official YouTube reused/inauthentic content, copyright, thumbnail impersonation, and realistic AI-content disclosure guidance. Do not offer a blanket legal guarantee.
```

## Multimodal visual grammar analysis

Analyze only the supplied images/frames. Do not infer unseen scenes, audio, creator intent, analytics, or audience response. For every observation, cite the asset filename and visible evidence. Separate OBSERVATION from INTERPRETATION and HYPOTHESIS. Describe composition, focal hierarchy, contrast, subject scale, text density, framing, visual continuity, and repeated visual grammar. Then derive five transferable principles and propose three original alternatives that do not reproduce the source composition or branding. Return a table with: asset, observation, evidence, interpretation, confidence, alternative explanation, adaptation.

## Video beat/shot analysis

Analyze only the video, frames, transcript, and audio that were actually supplied. Build a time-coded beat sheet with: time range, visible action/shot, narration/dialogue (summarize; do not reproduce long copyrighted passages), on-screen text, edit/transition, sound/music (only if heard), narrative function, evidence/confidence, and an original adaptation. Mark gaps as NOT OBSERVED. Do not claim full frame-by-frame coverage from a sparse contact sheet.

## Thumbnail/title packaging analysis

For each supplied thumbnail and its matching title, explain the title's promise, the image's complementary information, focal hierarchy, subject scale, contrast, mobile legibility, text density, curiosity mechanism, and possible mismatch/deception risk. Compare results only within appropriate format and upload-age groups. Produce three distinct original concepts using the learned principle, not the same layout, character, wording, or brand identity.
