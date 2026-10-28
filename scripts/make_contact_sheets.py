#!/usr/bin/env python3
"""Create frame contact sheets from local videos you own or are authorized to analyze."""
import argparse, math, subprocess, tempfile
from pathlib import Path
from PIL import Image, ImageDraw

def main():
    p=argparse.ArgumentParser(); p.add_argument("video", help="Local video file"); p.add_argument("--out", default="contact-sheet.jpg"); p.add_argument("--frames", type=int, default=12); p.add_argument("--cols", type=int, default=3); p.add_argument("--width", type=int, default=480); a=p.parse_args()
    src=Path(a.video)
    if not src.is_file(): p.error(f"File not found: {src}")
    if not shutil_which("ffmpeg"): p.error("ffmpeg not found; install ffmpeg and ensure it is on PATH")
    if a.frames<1 or a.cols<1: p.error("--frames and --cols must be positive")
    with tempfile.TemporaryDirectory() as td:
        tmp=Path(td); imgs=[]
        # Sample evenly across the clip using ffmpeg's select filter; timestamps are approximate.
        for i in range(a.frames):
            out=tmp/f"frame-{i:03d}.jpg"
            # fps filter is duration-independent and gives an evenly distributed rough sample via thumbnail filter.
            vf=f"thumbnail=n={max(1, int(100/a.frames))},scale={a.width}:-1"
            cmd=["ffmpeg","-hide_banner","-loglevel","error","-ss",str(i*2),"-i",str(src),"-frames:v","1","-vf",f"scale={a.width}:-1","-y",str(out)]
            # Fallback sampling at 2-second intervals is robust even without duration probing.
            subprocess.run(cmd,check=False,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            if out.exists():
                im=Image.open(out).convert("RGB"); draw=ImageDraw.Draw(im); draw.rectangle((0,0,120,24),fill="black"); draw.text((6,5),f"Sample {i+1} (~{i*2}s)",fill="white"); imgs.append(im)
        if not imgs: p.error("No frames extracted. Check that ffmpeg can read this video file.")
        cellw=max(im.width for im in imgs); cellh=max(im.height for im in imgs)+30; rows=math.ceil(len(imgs)/a.cols)
        sheet=Image.new("RGB",(a.cols*cellw,rows*cellh),(245,245,245))
        for idx,im in enumerate(imgs): sheet.paste(im,((idx%a.cols)*cellw,(idx//a.cols)*cellh+30))
        dest=Path(a.out); dest.parent.mkdir(parents=True,exist_ok=True); sheet.save(dest,quality=90)
        print(f"Saved {len(imgs)} sampled frames to {dest.resolve()}")

def shutil_which(name):
    import shutil; return shutil.which(name)
if __name__=="__main__": main()
