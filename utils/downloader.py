import os
import subprocess
import typing as t

from yt_dlp import YoutubeDL


def format_selector(ctx):
    """ Select the best video and the best audio that won't result in an mkv.
    NOTE: This is just an example and does not handle all cases """

    # formats are already sorted worst to best
    formats = ctx.get('formats')[::-1]

    # acodec='none' means there is no audio
    best_video = next(f for f in formats
                      if f['vcodec'] != 'none' and f['acodec'] == 'none')

    # find compatible audio extension
    audio_ext = {'mp4': 'm4a', 'webm': 'webm'}[best_video['ext']]
    # vcodec='none' means there is no video
    best_audio = next(f for f in formats if (
            f['acodec'] != 'none' and f['vcodec'] == 'none' and f['ext'] == audio_ext))

    # These are the minimum required fields for a merged format
    yield {
        'format_id': f'{best_video["format_id"]}+{best_audio["format_id"]}',
        'ext': best_video['ext'],
        'requested_formats': [best_video, best_audio],
        # Must be + separated list of protocols
        'protocol': f'{best_video["protocol"]}+{best_audio["protocol"]}'
    }


def find_file_recursive(start_dir: str, partial_name: str) -> str:
    """
      Finds files with names containing the given partial name in a directory structure.
      """
    matches = None
    for root, _, files in os.walk(start_dir):
        for filename in files:
            if partial_name.lower() in filename.lower():  # Case-insensitive search
                matches = os.path.join(root, filename)
    return matches


def download(urls: t.List[str]) -> str:
    ydl_opts = {
        'format': format_selector,
    }

    with YoutubeDL(ydl_opts) as dl:
        info = dl.extract_info(urls, download=False)
        subprocess.run(["yt-dlp", "-P", "./download/", f"{urls}"])
        find_file_path = find_file_recursive("./download/", info.get("id"))

    return find_file_path
