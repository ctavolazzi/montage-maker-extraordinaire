# montage-maker-extraordinaire

One command turns a folder of your clips into a captioned vertical video, ready to post.

```
montage --caption "Day 12 of building a robot farm"
montage --count 7
```

It picks a few clips at random, trims a short slice from each, crops them to 9:16,
stitches them together, burns in a caption, and saves the video plus a cover image to
`ready/`.

**Status:** scaffold only. The code in `montage/` is pseudocode (function signatures,
docstrings and step-by-step comments). Nothing runs yet. See `docs/PLAN.md`.

## Folder layout (at run time)

```
clips/         your source videos (camera roll synced to your computer, or a Drive folder)
music/         optional background tracks
captions.txt   optional, one caption per line (start from captions.example.txt)
ready/         finished videos and covers
.montage/      state: which clips have been used this cycle
```

## v1 features

- **Random pick:** N clips (default 4), each used once per cycle before any repeats.
- **Auto trim:** a random 2 to 4 second slice from each clip.
- **Vertical:** scale to cover 1080x1920, center crop.
- **Caption:** typed, or a random line from `captions.txt`. White text, black stroke, rounded
  black pill behind each line.
- **Music (optional):** random track from `music/`, original audio muted.
- **Batch:** `--count 7` makes a week of videos in one run.
- **Cover image:** a frame with the caption on it, saved next to each video.

## Dependencies

- `ffmpeg` and `ffprobe` on your PATH (does all cutting, cropping and stitching)
- Python 3.10+ and Pillow (draws the caption)

No MoviePy and no ImageMagick. See `docs/PRIOR-ART.md` for why.

## Docs

| File | What it is |
|---|---|
| `docs/PLAN.md` | The MVP: features, what is out of scope, build order |
| `docs/ARCHITECTURE.md` | Pipeline, modules, data flow, state file, ffmpeg commands |
| `docs/PRIOR-ART.md` | The existing tools whose code was read, and what is borrowed from each |
| `CLAUDE.md` | Rules for working in this repo |
