# MVP plan

Written 2026-10-30.

## Goal

One command turns a folder of your clips into a captioned vertical video, ready to post.
Saves the time of opening an editor, picking clips, trimming, cropping and typing a caption
for every short.

## How it works

1. You point it at a folder (your camera roll synced to your computer via iCloud or Google
   Photos, or a Drive folder).
2. It picks a few clips at random.
3. It trims, stacks, captions, and saves the finished video and a cover image to `ready/`.

## v1 features

| Feature | What it does | Borrowed from |
|---|---|---|
| Random pick | N clips (default 4). Each clip used once per cycle; when all are used, a new cycle starts | autoshorts (hash-based cycle tracking) |
| Auto trim | Random 2 to 4 second slice from a random start point in each clip | hdsa2019doc (random start and length) |
| Normalize | Every slice re-encoded to the same size, frame rate and pixel format before stitching | mikhin's gist (`-r 30`, re-encode before concat) |
| Vertical | Scale to cover 1080x1920, center crop the excess | MoneyPrinterTurbo (cover-and-crop) |
| Caption | Typed with `--caption`, or a random line from `captions.txt`. White text, black stroke, rounded black pill per line, auto word wrap | autoshorts (Pillow PNG + ffmpeg overlay) |
| Music | Optional random track from `music/`, original audio muted, trimmed to video length | vmashd, mikhin (`-shortest`) |
| Batch | `--count 7` makes 7 videos in one run | mikhin (`numberOfVideos`) |
| Cover image | One frame with the caption on it, saved as `<name>.jpg` next to the video | new (every video needs a thumbnail) |

## Usage

```
montage --caption "Day 12 of building a robot farm"
montage --count 7
montage --clips 5 --min 2 --max 3 --no-music
```

## Not in v1

- Auto posting (Postiz or Upload-Post API)
- Phone trigger (iOS Shortcut)
- AI-written captions
- Picking clips that match the caption (see slideshow-automation in `docs/PRIOR-ART.md`)
- Web UI
- Effects, transitions, beat sync

## Known risks

- **iPhone HDR and HEVC clips.** Often 10-bit HDR. Without a tone-map step they can look washed
  out after conversion. v1 detects HDR with ffprobe and either tone-maps or warns.
- **Rotation metadata.** Phone clips can be stored sideways with a rotate flag. Recent ffmpeg
  applies it automatically on decode; confirm on CT's footage.
- **Very short clips.** Clips shorter than the minimum slice are skipped, not stretched.
- **Captions on busy footage.** The pill background exists so text stays readable on any frame.

## Build order

1. `clip.py`: cut, normalize and crop one slice. Test on 3 of CT's real clips, including one
   iPhone HDR clip.
2. `build.py` concat: stitch slices into one silent video.
3. `caption.py` and the overlay step.
4. `pick.py` and `state.py`: random pick with cycle tracking.
5. Music, cover image, then `--count`.
6. `cli.py` wiring and a README usage check.

Each step is a working command before the next starts.
