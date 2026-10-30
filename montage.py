"""Folder of videos and photos in, vertical montage with text on top out.

    python montage.py my-folder --text "Day 12 of building a robot farm"

SCAFFOLD: every step below is pseudocode. Nothing runs yet.
"""

# ---------- settings ----------

PIECES = 4                 # how many clips/photos go in one montage
VIDEO_PIECE_SECONDS = 3    # how long each video piece is
PHOTO_SECONDS = 2          # how long each photo stays on screen
WIDTH, HEIGHT = 1080, 1920 # vertical
FPS = 30
OUTPUT_DIR = "output"

VIDEO_TYPES = [".mp4", ".mov", ".m4v"]
PHOTO_TYPES = [".jpg", ".jpeg", ".png", ".heic"]


# ---------- the steps ----------

def main():
    # folder, text = read the command line
    # files = find_media(folder)
    # chosen = pick(files)
    # pieces = [make_piece(f) for f in chosen]
    # joined = stitch(pieces)
    # final = add_text(joined, text)
    # save_thumbnail(final)
    # print where the video and thumbnail were saved
    pass


def find_media(folder):
    """Every video and photo in the folder."""
    # return files whose extension is in VIDEO_TYPES or PHOTO_TYPES
    # skip videos shorter than VIDEO_PIECE_SECONDS (ask ffprobe for the length)
    pass


def pick(files):
    """A random handful."""
    # shuffle files
    # return the first PIECES of them (or all of them if there are fewer)
    pass


def make_piece(file):
    """One short vertical video piece from a video or a photo."""
    # if it's a video:
    #     start = random point between 0 and (length - VIDEO_PIECE_SECONDS)
    #     ffmpeg: cut VIDEO_PIECE_SECONDS from start
    # if it's a photo:
    #     ffmpeg: hold the photo on screen for PHOTO_SECONDS
    #
    # both, in the same ffmpeg call:
    #     fill a WIDTH x HEIGHT frame, cut off the edges that don't fit
    #     set FPS, drop the sound
    #     save to a temp file
    #
    # the ffmpeg filter for the fill-and-crop part:
    #     scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,format=yuv420p
    pass


def stitch(pieces):
    """Join the pieces end to end."""
    # write a list file with one line per piece
    # ffmpeg -f concat -safe 0 -i list.txt -c copy joined.mp4
    pass


def add_text(video, text):
    """Put the text on top of the video."""
    # 1. Pillow: draw the text on a see-through image the width of the video
    #       white letters, black outline, dark rounded box behind each line
    #       wrap long text onto more lines
    # 2. ffmpeg: lay that image over the video near the top
    #       ffmpeg -i joined.mp4 -i text.png -filter_complex "overlay=0:H*0.12" output/montage.mp4
    pass


def save_thumbnail(video):
    """One frame of the finished video, text included, as a .jpg."""
    # ffmpeg -ss 1 -i output/montage.mp4 -frames:v 1 output/montage.jpg
    pass


if __name__ == "__main__":
    main()
