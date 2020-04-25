#!/bin/python3
import os
from requests import exceptions
from tempfile import mkdtemp
from time import sleep
from urllib.request import urlopen
from um3api import Ultimaker3
import shutil

HOST = input("UM3 IP address: ")
# HOST = "" # UM3 IP goes here

DELAY = int(input("Set delay (s)"))
# DELAY = int(5)

OUTFILE = input("Save file as <filename>.mp4/.mkv: ")
# OUTFILE = "test.mp4"

imgurl = "http://" + HOST + ":8080/?action=snapshot"

api = Ultimaker3(HOST, "Timelapse")

def printing():
	status = None
	# If the printer gets disconnected, retry indefinitely
	while status == None:
		try:
			status = api.get("api/v1/printer/status").json()

			if status == 'printing':
				state = api.get("api/v1/print_job/state").json()

				if state == 'wait_cleanup':
					return False

				else:
					return True
			else:
				return False
		except exceptions.ConnectionError as err:
			status = None
			print_error(err)

def progress():
	p = None
	# If the printer gets disconnected, retry indefinitely
	while p == None:
		try:
			p = api.get("api/v1/print_job/progress").json() * 100
			return "%05.2f %%" % (p)
		except exceptions.ConnectionError as err:
			print_error(err)

def print_error(err):
	print("Connection error: {0}".format(err))
	print("Retrying")
	print()
	sleep(1)
	clear_temp()

def clear_temp():
	# delete temp files
	print("Cleaning up temp files in ",tmpdir)
	shutil.rmtree(tmpdir)

tmpdir = mkdtemp()
filenameformat = os.path.join(tmpdir, "%05d.jpg")
print("Saving images to",tmpdir)

if not os.path.exists(tmpdir):
	os.makedirs(tmpdir)

print("Waiting for print to start")
while not printing():
	sleep(1)

print("Printing")
count = 0

while printing():
	count += 1
	response = urlopen(imgurl)
	filename = filenameformat % count
	f = open(filename,'bw')
	f.write(response.read())
	f.close()
	print("Print progress: %s Image: %05i" % (progress(), count), end='\r')
	sleep(DELAY)
	print()

print("Print completed.")
extra_frames = 0

while extra_frames < 4:
	sleep(DELAY)
	count += 1
	response = urlopen(imgurl)
	filename = filenameformat % count
	f = open(filename,'bw')
	f.write(response.read())
	f.close()
	extra_frames +=1
	sleep(3)

print("Encoding video")
ffmpegcmd = "ffmpeg -r 30 -i " + filenameformat + " -vcodec libx264 -preset veryslow -crf 18 " + OUTFILE + " -y" # uncomment -y flag to disable automatic outfile overwrite
print(ffmpegcmd)
os.system(ffmpegcmd)
clear_temp()