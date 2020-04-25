Ultimaker 3 Timelapse Maker
===========================

A script that makes timelapse videos from the onboard camera on your Ultimaker 3.

![Bulbasaur](https://thumbs.gfycat.com/EntireGlassAlaskanmalamute-size_restricted.gif)

Usage
-----

This script requires Python 3.5 or later and [FFmpeg](https://ffmpeg.org/).
Run the script. It will take some inputs and then wait for your Ultimaker to begin printing.
It will then start taking pictures.

When the print finishes, the script will compile all the snapshots it took into a video.
Video is encoded using H.264 at 30 fps, but you can easily change this by editing `ffmpegcmd` in the script.

To do
------

- Only take shots when state == "printing" and not during "pre_print"
- Take postroll shots when state == "post_print"
- Add check for ffmpeg at start

Thanks
------

[Ultimaker 3 API library](https://ultimaker.com/en/community/23329-inside-the-ultimaker-3-day-3-remote-access-part-2) by Daid