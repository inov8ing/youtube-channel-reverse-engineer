# Source and Data Protocol

## 1. Source hierarchy

Use sources in this order when they answer the question:

1. **Official platform documentation** for how YouTube search, recommendations, metrics, API access, thumbnails, AI disclosures, and monetization policies work.
2. **The target channel's own public assets**: channel page, About section, upload pages, thumbnails, descriptions, playlists, public comments, community posts, transcripts visible in the standard player, and live recordings.
3. **Primary sources relevant to the video's subject**: original research papers, official records, first-party company documentation, regulatory publications, interviews, or original datasets.
4. **Reliable secondary sources** for context and corroboration.
5. **Third-party creator analytics services** only as clearly labelled estimates when a historical series is useful. Do not represent their numbers as YouTube Studio data.
6. **LLM-generated analysis** is not source evidence. LLMs can classify, summarize, critique, and propose hypotheses from sourced material, but cannot create evidence.

## 2. Data access options

### Option A — YouTube Data API is available
Use documented endpoints and current quotas. For a specific channel:
- Resolve the channel using `channels.list` when possible.
- Read public channel metadata and statistics only from returned fields.
- Use `contentDetails.relatedPlaylists.uploads` to identify the channel's uploads playlist.
- Enumerate videos using `playlistItems.list` with pagination.
- Request relevant video fields in batches using `videos.list`, including `snippet`, `contentDetails`, and `statistics` where available.
- Reserve `search.list` for discovery and external topic searches; its quota bucket has a separate daily request limit. Re-check current quota documentation before any automated collection.
- Store request time, response timestamp, fields requested, and any missing/hidden values.

Do not treat unavailable fields as zero. Do not call undocumented endpoints or use scraping methods to get data that the documented API does not provide. The captions download method requires authorization and permission to edit that video; it is not a way to download arbitrary competitor captions.

### Option B — No API credentials
Use the available browser/search capability to inspect public channel and individual video pages manually. Record visible values with the collection date. Search results are discovery aids, not proof of complete channel coverage. State what you could and could not inspect.

### Option C — User supplies their own Analytics
If the user owns the channel and supplies Analytics exports/screenshots, analyze the supplied metrics separately and respect their chosen time windows. Do not compare different metrics with mismatched windows or combine data without explaining the definitions. For competitor channels, never pretend to have the owner's private Analytics.

## 3. Publicly visible versus private metrics

Usually visible to the public, subject to channel settings and endpoint availability:
- Current public view count.
- Current public subscriber count, potentially rounded.
- Public channel view total and public upload count.
- Video title, publication date, description, thumbnail, duration, and some public engagement counts.
- Visible playlists/sections, chapters, public comments, and transcripts when available.

Typically not visible for a competitor without authorized Analytics:
- Impressions and impressions click-through rate.
- Browse, Suggested, Search, External and other private traffic-source breakdowns.
- Audience retention curve, average view duration, watch time, engaged-view details in the owner's dashboard.
- Returning viewers, subscriber gains attributed to a video, audience age/gender/geography, device split, viewer satisfaction survey data.
- Paid promotion/spend, revenue, RPM/CPM, monetization eligibility or status.

Third-party websites may model some figures, but those are estimates with unknown error. Label them, date them, and keep them distinct from official public metrics. Never fabricate private metrics by reverse-engineering them from view counts, likes, upload times, or comments.

## 4. Time and format normalization

For every view-based observation, record:
- Public view count.
- Snapshot date/time and source.
- Publish date.
- Days since publication, calculated from the snapshot date.
- Format cohort, confirmed from visible evidence where possible.
- Topic/series cohort.

Prefer age-matched cohorts. A one-week-old Short should not be directly compared to a five-year-old tutorial as proof of quality. A lifetime average `views ÷ days since publication` is a crude descriptive measure, not current velocity. True measured velocity needs repeated snapshots, and even then it is a snapshot interval—not a statement of what the algorithm did.

Use caution around view-count definition changes. As of the current research snapshot, official YouTube Data API documentation says view counting for all formats began counting a view when a video begins to play from August 24, 2026, including autoplay, hold-pointer and click/tap playback. This makes it especially important not to compare counts from before and after that change without a clear caveat.

Do not infer Short status from duration alone. Use the platform's visible format label or direct evidence of format/aspect ratio when available. If format remains uncertain, mark it “unconfirmed.”

## 5. Sample design

A robust channel audit uses both the broad catalogue and detailed case studies.

For broad metadata, collect the available catalogue if practical. For creative review, stratify rather than cherry-pick:
- Top public-view examples.
- Most recent uploads.
- Typical-looking examples.
- Recent weaker examples.
- Repeated series or format variations.
- Standout outliers or timely uploads.

Review all uploads for a small channel. For a large channel, a default deep sample is 8–12 long-form videos or 12–20 Shorts, adjusted for variety. Report overlap between sample groups. Sample rules are practical operating guidance, not a statistically representative guarantee.

## 6. Evidence classifications

Use these labels consistently:

- `OBSERVED FACT`: directly visible, directly quoted (briefly), or returned by an official documented source.
- `CALCULATION`: arithmetic from named inputs, formula, cohort, and snapshot dates shown.
- `INTERPRETATION`: an explanation that fits the observed facts but is not uniquely proven.
- `HYPOTHESIS`: a testable idea to validate on the user's own channel.
- `UNKNOWN`: data not available or evidence too weak to support a claim.

Confidence is for the strength of evidence behind an interpretation—not a score for the creator, channel, or quality of their videos.

## 7. Permitted analytical posture

Good:
- “Six of the ten sampled high-view uploads use a visible challenge premise; this pattern is worth testing with an original premise.”
- “This video has more public views than most sampled recent uploads, but its older publication date, subject, and external attention may contribute.”
- “The opening quickly demonstrates the result. That may help align the packaging promise with the actual experience; private retention data would be needed to validate the effect.”

Bad:
- “Its CTR is 12%” without the owner's Analytics.
- “YouTube pushed it because retention was high” without evidence.
- “Upload at 7 PM and the algorithm will give more impressions.”
- “The channel has a 92/100 growth score” derived from public metrics.
- “This channel earns $X monthly” inferred from views.

## 8. API-policy care

Before using API-derived values, re-read current YouTube API developer policies. Do not use API data to estimate revenue, watch time, unique reach, demographics, audience affinity, satisfaction, monetization status, or other prohibited private metrics. Do not build a public cross-channel leaderboard or composite channel score from API data, and do not merge API data with external datasets to infer prohibited information. A strategy report can describe visible patterns without claiming it knows private analytics or the platform's internal model.

## 9. Research citations

For each material recommendation:
- Cite the direct public video/channel source when the claim concerns what the target actually did.
- Cite current official YouTube documentation when the claim concerns platform rules/metrics.
- Cite primary factual sources for script claims and include a source list in the final report.
- Keep claims proportional to what a source actually establishes. A source about title tips does not prove that one title will get more views.

## Optional local Python collection and visual workflow (V1)

Use `scripts/collect_channel.py` as an optional helper when the environment permits its collection method. It accepts one channel or video URL and produces a timestamped research folder with `channel-root.json`, `video-inventory.csv`, `run-manifest.json`, and a visual-analysis handoff file. Metadata-only is the default; thumbnail collection is opt-in. Video download requires both `--download-videos` and `--i-have-rights`. That flag is an acknowledgement only and does not establish permission or legal compliance.

When available and permitted, prefer documented YouTube Data API resources for systematic public metadata. `yt-dlp` may be useful for a local research pack, but its technical capability is not the same as platform authorization. If automated extraction is not permitted, do not run it; use official APIs, browser-visible public data, or user-provided materials. Never bypass controls, scrape at scale, or use undocumented endpoints.

For multimodal review, analyze actual thumbnail files with a vision-capable model. To analyze editing and video structure, use authorized local video files or other permitted source material; sample frames with `scripts/make_contact_sheets.py` or use a model's direct video input when supported. State precisely whether the review covered thumbnails, sampled frames, full video, transcript, or audio. Do not infer motion from stills or audio from silent frames. Model/API integration is deployment-specific; the skill must not pretend it has called a vision endpoint unless it actually did.
