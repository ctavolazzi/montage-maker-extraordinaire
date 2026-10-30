# montage-maker-extraordinaire

Put videos in a folder. Run one command. It picks random videos, clips them into a montage,
and puts your text over it. Then you post it.

```
python montage.py my-folder --text "Day 12 of building a robot farm"
```

Out comes `output/montage.mp4`.

## What it does

1. Picks random videos from your folder.
2. Clips a short piece from each.
3. Combines them into one montage.
4. Puts your text over it.

Your original files are never changed.

## Needs

- `ffmpeg`
- Python 3 with Pillow (`pip install pillow`)

## Status

Scaffold. `montage.py` has every step written out as pseudocode. Nothing runs yet.
