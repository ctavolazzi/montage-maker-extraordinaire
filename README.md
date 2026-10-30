# montage-maker-extraordinaire

Put videos and photos in a folder. Run one command. Get a vertical montage with your text on
top, ready to post.

```
python montage.py my-folder --text "Day 12 of building a robot farm"
```

Out comes `output/montage.mp4` and `output/montage.jpg` (the thumbnail).

## What it does

1. Grabs the videos and photos in your folder.
2. Shuffles them and takes a few.
3. Cuts a short piece from each video. Shows each photo for 2 seconds.
4. Makes every piece vertical (1080x1920).
5. Stitches them together.
6. Puts your text on top.
7. Saves the video and a thumbnail.

Your original files are never changed.

## Needs

- `ffmpeg`
- Python 3 with Pillow (`pip install pillow`)

## Status

Scaffold. `montage.py` has every step written out as pseudocode. Nothing runs yet.

## Later (not now)

Background music, making a week of videos at once, not repeating clips, auto posting.
