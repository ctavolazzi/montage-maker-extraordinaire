"""Thin wrappers around ffmpeg and ffprobe. Every other module goes through here."""

from dataclasses import dataclass
from pathlib import Path


@dataclass
class ClipInfo:
    duration_s: float
    width: int
    height: int
    is_hdr: bool          # color_transfer is smpte2084 (HDR10) or arib-std-b67 (HLG)


def check_installed() -> None:
    """Fail early with a clear message if ffmpeg or ffprobe is missing."""
    # for tool in (ffmpeg, ffprobe): if shutil.which(tool) is None: raise SystemExit(how to install)
    raise NotImplementedError


def run(args: list[str]) -> None:
    """Run ffmpeg quietly. Raise with the stderr text if it fails."""
    # cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", *args]
    # result = subprocess.run(cmd, capture_output=True, text=True)
    # if result.returncode != 0: raise RuntimeError(cmd + result.stderr)
    raise NotImplementedError


def probe(path: Path) -> ClipInfo:
    """Duration, size and HDR flag of the first video stream."""
    # out = ffprobe -v error -select_streams v:0
    #         -show_entries format=duration:stream=width,height,color_transfer -of json path
    # parse json
    # is_hdr = color_transfer in ("smpte2084", "arib-std-b67")
    # return ClipInfo(...)
    raise NotImplementedError


def has_filter(name: str) -> bool:
    """True if this ffmpeg build has a filter (used to check for zscale before tone mapping)."""
    # return name in output of `ffmpeg -hide_banner -filters`
    raise NotImplementedError
