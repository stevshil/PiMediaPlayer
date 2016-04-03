#!/usr/bin/python

from easygui import *
import sys
import subprocess
import random
import os
import ntpath
import select

def playme():
  mplayerargs=" -slave -input file=/tmp/myplay nogui -loop 0 -af volnorm=2:0.75 -playlist "+roplaylist
  player = subprocess.Popen(["mplayer", mplayerargs, audiofile], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  player.poll()
  return player

def playlistmix(theplaylist):
  #playlist=subprocess.Popen(["sort", "-R", theplaylist], stdout=subprocess.PIPE)
  playlist=os.popen("sort -R " + theplaylist).read()
  s=''
  tmplist=s.join(playlist)
  playlist=tmplist.split('\n')
  return playlist

title="Pi Kitchen Player"
img="rpi-icon.gif"
buttons=["<<",">\"",">>","X"]
roplaylist="playlist"
thelist=playlistmix(roplaylist)
maxFile=len(thelist)
curFile=0
isplaying=0
ispaused=0
songname=ntpath.basename(thelist[curFile])
controls=buttonbox(songname, image=img, choices=buttons)
mfifoplayer="/tmp/myplay"
os.mkfifo(mfifoplayer)
fifow=open(mfifoplayer,"w")
fifor=open(mfifoplayer,"r")

while controls != "X":
  if controls == "X":
    fifow.write("quit")
    sys.exit(0)

  if controls == ">\"":
    if isplaying == 0 and ispaused == 0:
      fifow.write("get_file_name")
      for line in fifor:
        songname=line
      isplaying=1
    elif isplaying == 1 and ispaused == 0:
      fifow.write("pause")
      ispaused=1
    elif isplaying == 1 and ispaused == 1:
      fifow.write("pause")
      ispaused=0
  if controls == ">>":
      fifow.write("")
  if controls == "<<":
      fifow.write("quit")
  # Show controls
  songname=ntpath.basename(thelist[curFile])
  controls=buttonbox(songname, image=img, choices=buttons)
