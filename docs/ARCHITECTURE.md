# Architecture

A straight pipeline. Each stage is one small module with one job. Stages pass file paths,
never video data in memory.

```
cli.py
  │  parse args, load config
  ▼
pick.py ──── state.py        choose N clips (cycle tracking by hash)
  │
  ▼
clip.py                      for each clip: random slice → normalize → 9:16 crop → temp .mp4
  │
  ▼
build.py                     concat slices → overlay caption PNG → add music → ready/<name>.mp4
  │   ▲
  │   └── caption.py         caption text → transparent PNG (Pillow)
  ▼
build.py (cover)             one frame + caption PNG → ready/<name>.jpg
```

## Modules

| Module | Job | Inputs | Output |
|---|---|---|---|
| `config.py` | Defaults and paths | CLI args, optional `montage.toml` | `Config` |
| `state.py` | Remember which clips were used this cycle | `.montage/state.json` | used hashes, cycle start |
| `pick.py` | Choose clips | clips folder, state, N | list of clip paths |
| `clip.py` | Make one vertical slice | clip path, slice length | temp slice path |
| `caption.py` | Draw caption PNG | text, width, font | PNG path |
| `build.py` | Assemble final video and cover | slice paths, caption PNG, music | `.mp4` and `.jpg` paths |
| `ffmpeg.py` | Run ffmpeg and ffprobe, raise on error | arg list | stdout or exception |
| `cli.py` | Wire it together, loop for `--count` | argv | printed output paths |

## State file

`.montage/state.json`

```json
{
  "cycle_started_at": "2026-10-30T09:30:00",
  "used": {
    "<sha256 of file>": {"name": "IMG_1234.MOV", "last_used_at": "2026-10-30T09:31:02"}
  }
}
```

A clip is available if its hash is not in `used`, or its `last_used_at` is before
`cycle_started_at`. When fewer than N clips are available, start a new cycle.

## ffmpeg commands (planned)

Probe a clip:

```
ffprobe -v error -show_entries format=duration:stream=width,height,color_transfer -of json IN
```

One slice, normalized and cropped to 9:16 (cover-and-crop):

```
ffmpeg -y -ss START -t LEN -i IN
  -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,format=yuv420p,setsar=1"
  -an -c:v libx264 -preset veryfast -crf 20 SLICE.mp4
```

HDR source (color_transfer is `smpte2084` or `arib-std-b67`): add a tone-map step before scale
(`zscale` + `tonemap`), if the local ffmpeg build has `zscale`; otherwise warn.

Stitch slices (all already identical in format):

```
ffmpeg -y -f concat -safe 0 -i list.txt -c copy JOINED.mp4
```

Caption overlay plus optional music:

```
ffmpeg -y -i JOINED.mp4 -i CAPTION.png [-i MUSIC]
  -filter_complex "[0:v][1:v]overlay=0:H*0.12"
  [-map 2:a -shortest -c:a aac]
  -c:v libx264 -preset veryfast -crf 20 -movflags +faststart OUT.mp4
```

Cover image (frame at 1 s with the caption already burned in):

```
ffmpeg -y -ss 1 -i OUT.mp4 -frames:v 1 -q:v 2 OUT.jpg
```

## Naming

`ready/2026-10-30_0931_01.mp4` and `ready/2026-10-30_0931_01.jpg` (date, time, index in batch).
