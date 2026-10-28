#!/usr/bin/env python3
"""Collect a research starter pack for a YouTube channel URL.

Default mode is metadata-only. This script does not download video files.
It uses yt-dlp's metadata extractor, which may be subject to YouTube's terms,
applicable law, and yt-dlp's own support limitations. Use only where permitted.
"""
from __future__ import annotations
import argparse, csv, json, re, shutil, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

FIELDS = ["id", "title", "webpage_url", "channel", "channel_id", "channel_url",
          "upload_date", "release_timestamp", "duration", "view_count", "like_count",
          "comment_count", "description", "tags", "categories", "thumbnail", "availability"]

def safe_slug(s: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9._-]+", "-", s).strip("-.")
    return (s or "youtube-channel")[:80]

def main():
    p = argparse.ArgumentParser(description="Build a metadata/thumbnail research pack from one YouTube channel URL.")
    p.add_argument("channel_url", help="YouTube channel URL or a video URL from that channel")
    p.add_argument("--out", default="channel-research", help="Output root directory (default: channel-research)")
    p.add_argument("--limit", type=int, default=100, help="Maximum videos to inspect (default: 100; use 0 for all available)")
    p.add_argument("--download-thumbnails", action="store_true", help="Download public thumbnails for visual analysis")
    p.add_argument("--download-videos", action="store_true", help="Download media only when you have rights/permission")
    p.add_argument("--i-have-rights", action="store_true", help="Required acknowledgement for --download-videos")
    p.add_argument("--include-auto-subs", action="store_true", help="Request English auto captions where available; availability varies")
    args = p.parse_args()
    if args.download_videos and not args.i_have_rights:
        p.error("--download-videos requires --i-have-rights. Prefer metadata-only analysis for third-party channels.")
    if args.limit < 0: p.error("--limit must be >= 0")
    try:
        import yt_dlp
    except ImportError:
        print("Missing dependency. Install with: python -m pip install -r requirements.txt", file=sys.stderr); return 2

    out_root = Path(args.out)
    out_root.mkdir(parents=True, exist_ok=True)
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    # Metadata extraction: no video download by default. Flat playlist gives catalogue IDs,
    # then individual metadata calls add richer public fields while limiting requests.
    opts = {"quiet": True, "no_warnings": True, "extract_flat": "in_playlist", "skip_download": True,
            "ignoreerrors": True, "playlistend": args.limit if args.limit else None}
    opts = {k:v for k,v in opts.items() if v is not None}
    with yt_dlp.YoutubeDL(opts) as ydl:
        root = ydl.extract_info(args.channel_url, download=False)
    if not root:
        print("Could not resolve this URL. Check that it is public and supported by your installed yt-dlp version.", file=sys.stderr); return 1
    channel_name = root.get("channel") or root.get("uploader") or root.get("title") or "youtube-channel"
    slug = safe_slug(channel_name)
    out = out_root / f"{slug}-{run_id}"
    out.mkdir(parents=True, exist_ok=True)
    (out / "channel-root.json").write_text(json.dumps(root, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    entries = root.get("entries") or []
    if not entries and root.get("id") and root.get("webpage_url"):
        entries = [root]
    # Re-fetch a bounded sample to obtain full public metadata. No media downloaded unless explicit opt-in.
    full_opts = {"quiet": True, "no_warnings": True, "skip_download": not args.download_videos,
                 "ignoreerrors": True, "writethumbnail": args.download_thumbnails,
                 "outtmpl": str(out / "%(upload_date)s_%(id)s_%(title).100B.%(ext)s")}
    if args.download_videos:
        full_opts["format"] = "bestvideo*+bestaudio/best"
    if args.include_auto_subs:
        full_opts.update({"writesubtitles": True, "writeautomaticsub": True, "subtitleslangs": ["en.*"], "subtitlesformat": "vtt/best"})
    rows = []
    manifest = {"input_url": args.channel_url, "channel_name": channel_name, "research_timestamp_utc": run_id,
                "yt_dlp_version": getattr(yt_dlp.version, "__version__", "unknown"), "limit": args.limit or "all",
                "video_download_enabled": bool(args.download_videos), "thumbnail_download_enabled": args.download_thumbnails,
                "items_seen": len(entries), "notes": ["Public metadata can be incomplete or unavailable.",
                "Views/likes/comments are snapshots, not historical growth or private analytics.",
                "Only download videos/captions where legally and contractually permitted."]}
    with yt_dlp.YoutubeDL(full_opts) as ydl:
        for i, entry in enumerate(entries, 1):
            if not entry: continue
            url = entry.get("webpage_url") or entry.get("url")
            if not url:
                vid = entry.get("id")
                if vid: url = f"https://www.youtube.com/watch?v={vid}"
            if not url: continue
            print(f"[{i}/{len(entries)}] Reading metadata: {entry.get('title','(untitled)')}", file=sys.stderr)
            try:
                info = ydl.extract_info(url, download=args.download_videos)
            except Exception as e:
                info = {"id": entry.get("id"), "title": entry.get("title"), "webpage_url": url, "_collection_error": str(e)}
            if not info: continue
            row = {k: info.get(k) for k in FIELDS}
            row["tags"] = json.dumps(row.get("tags") or [], ensure_ascii=False)
            row["categories"] = json.dumps(row.get("categories") or [], ensure_ascii=False)
            rows.append(row)
    with (out / "video-inventory.csv").open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS + ["_collection_error"], extrasaction="ignore")
        writer.writeheader(); writer.writerows(rows)
    (out / "run-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    (out / "VISUAL-ANALYSIS-INSTRUCTIONS.md").write_text(f'''# Visual analysis handoff\n\nChannel: {channel_name}\nResearch run: {run_id}\n\n1. Inspect `video-inventory.csv` and the thumbnails in this folder (if downloaded).\n2. Use a vision-capable model to analyze thumbnails in batches of 8–16. Ask it to report composition, focal hierarchy, subject scale, contrast, color relationships, text density, visual promise, and title-thumbnail complementarity.\n3. For video-level visual analysis, use only videos you own or have permission to analyze/download. Extract representative frames locally with the included `make_contact_sheets.py` script. Do not infer motion or editing from thumbnails alone.\n4. Label all observations as observed facts; label causal claims as hypotheses.\n\nDo not copy exact thumbnail compositions, distinctive characters, branding, scripts, music, or creator likeness. Derive reusable design principles and create original executions.\n''', encoding="utf-8")
    print(f"Research pack created: {out.resolve()}")
    print(f"Videos inventoried: {len(rows)}")
    print("Next: inspect run-manifest.json, video-inventory.csv, then follow VISUAL-ANALYSIS-INSTRUCTIONS.md")
    return 0
if __name__ == "__main__": raise SystemExit(main())
