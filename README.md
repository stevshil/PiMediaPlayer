OVERVIEW
========
A simple media player for the Raspberry Pi, based on using Raspbian as the main OS and mplayer to play the music.

2 versions:
* Console - runs on start up and will continually run, using a playlist generated from the music located in the $HOME/PiMusic folder.  It randomises the playlist through mplayer, and checks for new music each time it starts.  The cron job is used to enure that if the player stops that it starts within a minute.
* PiGUI - Currently a work in progress, but for use with a touch screen on the Pi

The PiGUI makes use of mplayer running in slave mode and sends the key presses to mplayer.

The player runs through a playlist located in the PiMusic where the actual music is also located.  On start up, or after the end of a playlist the playlist is randomised so that the list is different each time, and so that you don't get the same track twice like some random playlists, unless you have it in your music folder more than once.

You'll also notice some hidden folders which contain some configuration files needed to make the player start up when the system loads.

You should use Raspbian running LXDE with mplayer installed and Python 2.7.
