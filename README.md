# YouTube Channel Reverse Engineer

Turn a public YouTube channel into an evidence-led strategy blueprint — and an original launch plan that is not a copy of the channel you studied.

Give an AI assistant this repository (or just `SKILL.md`) plus one YouTube channel or video URL, and it researches the channel's public footprint, separates what is actually observed from what is only a hypothesis, and produces a blueprint for building a distinct channel serving a related audience.

## What it produces

- **Positioning:** what the channel promises, who it is for, and what repeatable content system it uses.
- **Topic and format map:** which topics, formats, series, and packaging patterns appear to work, compared like with like (Shorts against Shorts, long-form against long-form, age-matched where possible).
- **Creative teardown:** structure, pacing, titles, thumbnails, descriptions, and chapters — as design principles to adapt, never as material to copy.
- **Original channel blueprint:** a new promise, audience, content pillars, repeatable series, production model, and editorial standards.
- **First 10 video ideas** plus a full production pack for video #1.
- **A 30/60/90-day testing plan** with experiments, not guarantees.

## How to use it

1. Give the skill a YouTube channel URL, handle, or a video URL from the target channel.
2. Ask for the **Full Channel Blueprint** (the default), or pick a mode:

| Mode | What you get |
| --- | --- |
| Full Channel Blueprint (default) | The complete report: audit, teardown, blueprint, first videos, testing plan |
| Quick Audit | Positioning, strongest observed patterns, major risks, next five actions |
| Video Deep Dive | Beat-by-beat analysis of selected videos |
| Topic Engine | Ranked shortlist of original topic ideas, with evidence and packaging |
| Launch Blueprint | Positioning, first 10–30 videos, setup checklist, initial experiments |
| Update Audit | Refresh of an existing blueprint against new public data |
| Multi-Channel Benchmark | Qualitative comparison across channels (no leaderboard, no composite score) |

3. Supply your own constraints when you know them — language, target market, format, budget, hours per week, face or no-face. If you do not, the skill proceeds with labelled assumptions instead of interrogating you first.
4. For a diagnosis of your **own** channel, export your YouTube Studio analytics. Public data on a competitor can never reveal impressions, click-through rate, retention, traffic sources, demographics, or revenue, and this skill never pretends otherwise.

## Evidence discipline

Every material claim in a report carries one of these labels:

- `OBSERVED FACT` — directly visible or returned by an official documented source.
- `CALCULATION` — arithmetic from named inputs, with the formula and snapshot dates shown.
- `INTERPRETATION` — an explanation that fits the facts but is not uniquely proven.
- `HYPOTHESIS` — a testable idea to validate on your own channel.
- `UNKNOWN` — data that is not available or too weak to support a claim.

A partial but honest analysis is better than an invented complete one. If a metric is not publicly visible, the report says so.

## Optional: automated collection (V1 extension)

`SKILL.md` includes an optional Python workflow for richer evidence:

```bash
# Metadata-only research pack (default: up to 100 videos, no video downloads)
python scripts/collect_channel.py "https://www.youtube.com/@CHANNELHANDLE"

# Also save public thumbnails for visual inspection
python scripts/collect_channel.py "https://www.youtube.com/@CHANNELHANDLE" --download-thumbnails
```

The collector writes a timestamped folder under `channel-research/` containing `channel-root.json`, `video-inventory.csv`, `run-manifest.json`, and `VISUAL-ANALYSIS-INSTRUCTIONS.md`. Downloaded thumbnails can then be reviewed with a vision-capable model in batches, following the visual-analysis protocol in `SKILL.md`. Frame contact sheets for videos you own or are authorised to analyse can be made with:

```bash
python scripts/make_contact_sheets.py "path/to/authorised-video.mp4" --out "contact-sheet.jpg" --frames 12
```

Requirements: Python 3.11+, and FFmpeg if you plan to make contact sheets. Install dependencies with `pip install -r scripts/requirements.txt`.

## What this skill will not do

- Copy scripts, exact thumbnail compositions, branding, characters, voices, likenesses, catchphrases, or footage.
- Recommend fake engagement, bots, bought views, keyword stuffing, deceptive thumbnails, comment spam, or impersonation.
- Promise a number of views, subscribers, or a viral result. The recommendation system is personalised and not fully observable; the goal is better decisions through evidence and controlled learning.
- Download third-party videos, subtitles, or other assets without rights or permission. Video download in the collector is a separate explicit opt-in (`--download-videos --i-have-rights`), and that flag is an operator acknowledgement, not a legal determination.
- Scrape at scale, bypass access controls, use undocumented endpoints, or collect personal data about commenters. Where automated extraction is not permitted in your context, use the official YouTube Data API, browser-visible public information, or user-supplied files instead.

## What's in this repository

| Path | Contents |
| --- | --- |
| `SKILL.md` | The complete skill: role, workflow, output contract, visual-analysis protocol, guardrails, QA |
| `scripts/collect_channel.py` | Optional metadata-first channel inventory (yt-dlp; metadata-only by default) |
| `scripts/make_contact_sheets.py` | Frame contact sheets from local video files you own or are authorised to analyse |
| `scripts/requirements.txt` | Python dependencies (yt-dlp, Pillow) |
| `references/source-and-data-protocol.md` | Source hierarchy, collection methods, sample design, metric limits, policy care |
| `references/report-template.md` | The structured final-report template |
| `references/prompt-library.md` | Reusable prompts for topic research, scripting, production, thumbnails, metadata QA, analytics diagnosis, and originality review |
| `references/sources.md` | Official source register and current collection-policy references |
| `templates/video-inventory.csv` | Columns for cataloguing public video metadata and creative observations |
| `templates/evidence-ledger.csv` | Columns for tracing every claim back to its evidence |

## A note on the collector and platform terms

The Python collector is an optional local helper, not a guarantee that a collection method is permitted in every context. Follow YouTube's terms, applicable law, and API/developer policies. If automated extraction is not permitted where you run it, use documented APIs, browser-visible public information, or user-supplied data instead. Public competitor data never reveals impressions, CTR, retention, traffic-source splits, revenue, or demographics.
