#!/bin/bash

# Commands
# pt_step 1 (>)		forward in playlist
# quit (q)		exit player
# pause (p)		pause playback
# get_file_name		Gets current playing file
# http://cpansearch.perl.org/src/GBROWN/Gtk2-Ex-MPlayerEmbed-0.02/mplayer-slave-spec.txt

# Set the directory for the file playlist
if [[ "$1" == "DEBUG" ]]
then
  if [[ "$2" == "FULL" ]]
  then
    MUSICDIR="../ignore/music-full"
  else
    MUSICDIR="../ignore/music"
  fi
	PLAYLIST="../ignore/playlist"
	MIXED="../ignore/mixedlist"
	VOL="1:0.25 -softvol -volume 4"
else
	MUSICDIR="$HOME/PiMusic"
	PLAYLIST="$HOME/PiMusic/playlist"
	MIXED="$HOME/PiMusic/mixedlist"
	VOL="2:0.75"
fi

# Valid audio files mixed cases, playlist generator
# mp3 m4a ogg wav wma
find $MUSICDIR -type f | egrep -i '(mp3|m4a|ogg|wav|wma)$' > $PLAYLIST

# Set pulseaudio
if ps -ef | grep -v pulseaudio | grep -v grep >/dev/null 2>&1
then
        pulseaudio >/dev/null 2>&1 &
fi

realquit=0
echo "Randomising play list"
sort --random-sort $PLAYLIST > $MIXED
#perl -MList::Util -e 'print List::Util::shuffle <>' $PLAYLIST > $MIXED

# ./PiMplayer
# PiMplayer now calls this file
