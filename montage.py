"""Montage Maker.

Upload videos to your "Montage Maker" folder in Google Drive. Press the button.
A montage shows up in "Montage Maker/Montages". Press again for another one.

    python montage.py

Runs on your computer. Google Drive for desktop keeps the folder synced, so the script
just reads and writes a normal folder. No Google login code, no API, no cost.

The button is a small web page:
    on the computer:  http://localhost:8000
    on your phone:    http://<computer-name>.local:8000  (same Wi-Fi)

SCAFFOLD: every step below is pseudocode. Nothing runs yet.
"""

# ---------- fixed choices (no settings to fiddle with) ----------

FOLDER_NAME = "Montage Maker"   # the folder you upload to in Google Drive
OUTPUT_NAME = "Montages"        # made inside it, montages land here
MAX_CLIPS = 8                   # most videos used in one montage
CLIP_SECONDS = 3
WIDTH, HEIGHT, FPS = 1080, 1920, 30   # vertical, ready to post
VIDEO_TYPES = [".mp4", ".mov", ".m4v"]


# ---------- the button ----------

def main():
    # folder = find_drive_folder()
    # make folder/OUTPUT_NAME if it isn't there
    # start a tiny web server (Python's built-in http.server) on port 8000
    # GET /      -> a page with one big button: "Make a montage"
    # POST /make -> make_montage(folder), then show "Done: <file name>"
    pass


def find_drive_folder():
    """Where Google Drive for desktop keeps 'My Drive' on this computer."""
    # try, in order:
    #   Mac:      ~/Library/CloudStorage/GoogleDrive-*/My Drive/FOLDER_NAME
    #   Windows:  G:/My Drive/FOLDER_NAME
    #   older:    ~/Google Drive/FOLDER_NAME
    # if none exist: stop with "Install Google Drive for desktop and make a folder
    #                called Montage Maker in My Drive"
    pass


# ---------- making one montage ----------

def make_montage(folder):
    """One press = one new montage."""
    # videos = find_videos(folder)                       # skip the Montages folder
    # chosen = random.sample(videos, up to MAX_CLIPS)    # new mix every press
    # clips = [make_clip(v, best_moment(v)) for v in chosen]
    # combine(clips, folder/OUTPUT_NAME/"montage-<date>-<time>.mp4")
    # check the result isn't missing or short, delete temp files
    pass


def find_videos(folder):
    """Every video in the folder long enough to clip (ffprobe for the length)."""
    pass


def best_moment(video):
    """Pick where in the video to cut from. Free, runs on the computer.

    v1, no AI: ffmpeg's built-in scene and brightness measurements.
        ffmpeg -i video -vf "select='gt(scene,0)',signalstats,metadata=print" -f null -
        score each second: more movement = better, too dark or blown out = worse
        keep the top 3 moments, pick one at random (so a second press can differ)

    v2, free local AI (if v1 isn't good enough): grab one frame per second and score
    each with a free image-quality model from Hugging Face, run on this computer.
    Same output: a start time. Nothing else in the script changes.
    """
    pass


def make_clip(video, start):
    """CLIP_SECONDS from start, vertical, one ffmpeg command."""
    # ffmpeg -ss start -i video -t CLIP_SECONDS
    #   -vf scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,
    #       scale=out_color_matrix=bt709:out_range=tv,fps=30,setsar=1,format=yuv420p
    #   -an -c:v libx264 -crf 18 temp.mp4
    pass


def combine(clips, out):
    """Join the clips. Decoding join so no frames get dropped at the seams."""
    # ffmpeg -i clip1 -i clip2 ...
    #   -filter_complex "[0:v][1:v]...concat=n=<count>:v=1:a=0[v]"
    #   -map [v] -c:v libx264 -crf 20 -pix_fmt yuv420p -movflags +faststart out
    pass


if __name__ == "__main__":
    main()
