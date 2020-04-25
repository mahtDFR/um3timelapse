Ultimaker 3 timelapse maker
===========================

A script that makes timelapse videos from the onboard camera on your Ultimaker 3.

![Bulbasaur](https://thumbs.gfycat.com/EntireGlassAlaskanmalamute-size_restricted.gif)

Prerequisites
-----

- Python 3.5 or later
- [FFmpeg](https://ffmpeg.org/)

Usage
----

Run the script. It will take some inputs and then wait for your Ultimaker to begin printing.
It will then start taking pictures.

When the print finishes, the script will compile all the snapshots it took into a video.
Video is encoded using H.264 at 30 fps, but you can easily change this by editing `ffmpegcmd` in the script.

To do
------

- Only take shots when state == "printing" and not == "pre_print"
- Take postroll shots when state == "post_print"
- Add check for ffmpeg at start
- Take frames on Z moves only?