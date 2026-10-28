# Source Register

**Checked:** 2026-10-28. Re-check live policies and metric definitions whenever the skill is run; these pages and rules can change.

## Official YouTube/Google sources

1. [YouTube's Recommendation System](https://support.google.com/youtube/answer/16533387) — personalization, viewer satisfaction, and performance signals.
2. [Understand your content performance for YouTube's recommendation system](https://support.google.com/youtube/answer/16559650) — appeal, engagement, satisfaction; packaging and opening guidance; tags' limited role.
3. [YouTube performance FAQ & troubleshooting](https://support.google.com/youtube/answer/141805) — ranking context, upload cadence, breaks, timing, and retention considerations.
4. [How YouTube Search works](https://support.google.com/youtube/answer/16090438) — relevance, engagement, and quality.
5. [Thumbnail & title tips](https://support.google.com/youtube/answer/12340300) — accurate title/thumbnail design, clarity, audience framing, and using Analytics.
6. [Understand your YouTube video reach](https://support.google.com/youtube/answer/9314355) — public and owner-facing reach metric definitions, including impressions and CTR.
7. [Understand your YouTube content performance](https://support.google.com/youtube/answer/12220281) — definitions of performance metrics.
8. [Upload schedule tips](https://support.google.com/youtube/answer/13616979) — sustainable schedule planning.
9. [Tips to learn what viewers are watching](https://support.google.com/youtube/answer/13616337) — audience research available to a channel owner in Analytics.
10. [A/B test titles & thumbnails](https://support.google.com/youtube/answer/16391400) — current native testing availability, process, and watch-time outcome. Verify eligibility/features at run time.
11. [YouTube Data API: Channels resource](https://developers.google.com/youtube/data/reference/rest/v3/channels) — public channel resource fields and statistics.
12. [YouTube Data API: Videos resource](https://developers.google.com/youtube/data/reference/rest/v3/videos) — video metadata and statistics.
13. [YouTube Data API: Search list](https://developers.google.com/youtube/data/reference/rest/v3/search/list) — search resource and quota behavior.
14. [YouTube Data API quota calculator](https://developers.google.com/youtube/data/determine_quota_cost) — current default quotas and API method costs.
15. [YouTube API Services Developer Policies](https://developers.google.com/youtube/terms/developer-policies) — documented access, scraping prohibition, API-data use limits.
16. [Complying with YouTube's Developer Policies](https://developers.google.com/youtube/terms/developer-policies-guide) — prohibited estimates, cross-channel rankings/scores, and permitted descriptive metrics.
17. [YouTube captions.download API](https://developers.google.com/youtube/data/reference/rest/v3/captions/download) — authorization requirements; requires permission to edit the video.
18. [View video transcripts](https://support.google.com/youtube/answer/15930243) — viewer-accessible transcript feature when a video has captions.
19. [Thumbnail policy](https://support.google.com/youtube/answer/9229980) — misleading imagery, impersonation, and branding restrictions.
20. [YouTube channel monetization policies](https://support.google.com/youtube/answer/1311392) — original/authentic, reused and inauthentic-content rules.
21. [Copyright on YouTube](https://support.google.com/youtube/answer/2797466) — copyright basics and ways to use material; no option guarantees avoiding claims.
22. [Disclosing use of GenAI content](https://support.google.com/youtube/answer/14328491) — disclosure of realistic generated or meaningfully altered content.
23. [Add tags to your YouTube videos](https://support.google.com/youtube/answer/146402) — tags are mainly useful for common misspellings and have a minimal discovery role.

## Specific current caveat verified in API docs

The current `channels` and `videos` API resource documentation notes that, starting August 24, 2026, view counting across formats is updated to count views when a video begins to play, including autoplay, pointer hold, and click/tap playback. As the date is recent relative to many historical screenshots and third-party trend charts, report observation dates and do not silently combine different counting regimes.

## General research practice

For a niche-specific video, add sources for its factual content separately. Prefer original studies, official records, direct interviews, and first-party documentation. The source register above describes YouTube mechanics; it does not independently establish that any one creative tactic will succeed for any particular channel.

## Added for V1 automated collection and visual analysis

24. [yt-dlp official repository and README](https://github.com/yt-dlp/yt-dlp) — supported options for metadata extraction, JSON output, thumbnail files, subtitles, playlist/channel URLs, and behavior changes. Check the current README and installed version before use.
25. [YouTube Data API overview](https://developers.google.com/youtube/data/getting-started) — documented API access, quota, and resource retrieval.
26. [PlaylistItems: list](https://developers.google.com/youtube/data/reference/rest/v3/playlistItems/list) — documented playlist enumeration for a channel's uploads playlist.
27. [Videos: list](https://developers.google.com/youtube/data/reference/rest/v3/videos/list) — documented public video resource fields.
28. [YouTube Terms of Service](https://www.youtube.com/t/terms) — restrictions around automated access, downloading, reproduction, and use of content; verify the current applicable terms before any automated workflow.

The inclusion of yt-dlp as an optional local helper is not an assertion that any particular automated collection or downloading workflow is authorized. Deployment context, current platform terms, applicable law, and rights/permission matter. The script defaults to metadata-only and requires an explicit operator acknowledgement before downloading video media.
