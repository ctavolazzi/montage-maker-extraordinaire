"""Folder of videos in, montage with your text over it out.

    python montage.py my-folder --text "Day 12 of building a robot farm"

SCAFFOLD: every step below is pseudocode. Nothing runs yet.
"""

# ---------- settings ----------

CLIPS = 4                  # how many videos go in one montage
CLIP_SECONDS = 3           # how long each clip is
WIDTH, HEIGHT = 1080, 1920 # vertical, for posting
FPS = 30
OUTPUT = "output/montage.mp4"

VIDEO_TYPES = [".mp4", ".mov", ".m4v"]


# ---------- the steps ----------

def main():
    # folder, text = read the command line
    # videos = find_videos(folder)
    # chosen = pick_random(videos)
    # clips = [make_clip(v) for v in chosen]
    # joined = combine(clips)
    # add_text(joined, text)
    # print where the montage was saved
    pass


def find_videos(folder):
    """Every video in the folder."""
    # return files whose extension is in VIDEO_TYPES
    # skip videos shorter than CLIP_SECONDS (ask ffprobe for the length)
    pass


def pick_random(videos):
    """A random handful."""
    # shuffle videos
    # return the first CLIPS of them (or all of them if there are fewer)
    pass


def make_clip(video):
    """One short vertical clip from a video."""
    # start = random point between 0 and (length - CLIP_SECONDS)
    # ffmpeg, one call:
    #     cut CLIP_SECONDS from start
    #     fill a WIDTH x HEIGHT frame, cut off the edges that don't fit
    #     set FPS, drop the sound
    #     save to a temp file
    #
    # the ffmpeg filter for the fill-and-crop part:
    #     scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,format=yuv420p
    pass


def combine(clips):
    """Join the clips end to end."""
    # write a list file with one line per clip
    # ffmpeg -f concat -safe 0 -i list.txt -c copy joined.mp4
    pass


def add_text(video, text):
    """Put the text over the video."""
    # 1. Pillow: draw the text on a see-through image the width of the video
    #       white letters, black outline, dark rounded box behind each line
    #       wrap long text onto more lines
    # 2. ffmpeg: lay that image over the video near the top, save to OUTPUT
    #       ffmpeg -i joined.mp4 -i text.png -filter_complex "overlay=0:H*0.12" output/montage.mp4
    pass


if __name__ == "__main__":
    main()
