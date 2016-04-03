#!/usr/bin/python

from easygui import *
import sys
import subprocess
import random
import os
import ntpath
import select

def play(audiofile):
  mplayerargs="nogui -loop 0 -af volnorm=2:0.75 "+audiofile
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

#afile="/Data/Music/Ottawan - D.I.S.C.O. (1979).mp3"
title="Pi Kitchen Player"
img="rpi-icon.gif"
buttons=["<<",">\"",">>","X"]
isplaying=0
ispaused=0
#roplaylist=os.environ['HOME']+"/PiMusic/playlist"
roplaylist="playlist"
thelist=playlistmix(roplaylist)
maxFile=len(thelist)
curFile=0
songname=ntpath.basename(thelist[curFile])
curpid=0
controls = ">\""

while controls != "X":
  if controls == "X":
    playing.stdin.write("q")
    sys.exit(0)

  if controls == ">\"":
    if isplaying == 0 and ispaused == 0:
      playing=play(thelist[curFile])
      isplaying=1
      curpid=playing.pid
    elif isplaying == 1 and ispaused == 0:
      playing.stdin.write("p")
      ispaused=1
    elif isplaying == 1 and ispaused == 1:
      playing.stdin.write("p")
      ispaused=0
  if controls == ">>":
    if playing.poll() is None:
      playing.stdin.write("q")
    curFile+=1
    playing=play(thelist[curFile])
    curpid=playing.pid
  if controls == "<<":
    if playing.poll() is None:
      playing.stdin.write("q")
    curFile-=1
    playing=play(thelist[curFile])
    curpid=playing.pid

  if curpid != playing.pid and isplaying == 1 and ispaused == 0:
    playing=play(thelist[curFile])
    isplaying=1
    curpid=playing.pid

  # Show controls
  songname=ntpath.basename(thelist[curFile])
  controls=buttonbox(songname, image=img, choices=buttons)
