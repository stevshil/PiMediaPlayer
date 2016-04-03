OVERVIEW
========
A simple media player for the Raspberry Pi, based on using Raspbian as the main OS and mplayer to play the music.

2 versions:
* Console - runs on start up and will continually run, using a playlist generated from the music located in the $HOME/PiMusic folder.  It randomises the playlist through mplayer, and checks for new music each time it starts.  The cron job is used to enure that if the player stops that it starts within a minute.
* PiGUI - Currently a work in progress, but for use with a touch screen on the Pi
