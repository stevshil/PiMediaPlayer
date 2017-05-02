#!/bin/bash

apt-get -y update
apt-get -y upgrade
apt-get -y install lxde-core lxde task-lxde-desktop python-pip python-tk python-dev libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev mplayer pulseaudio
update-alternatives --config x-session-manager

pip install pillow

# Add pi user
if ! grep '^pi:' /etc/passwd >/dev/null 2>&1
then
	useradd -m -s /bin/bash pi
	(sleep 2; echo secret; sleep 2; echo secret) | passwd pi
fi
if ! grep '^pi' /etc/sudoers >/dev/null 2>&1
then
	echo "pi	ALL=(ALL:ALL) NOPASSWD: ALL" >>/etc/sudoers
fi

# Set pi user to login as default
sed -i 's/#autologin-user=/autologin-user=pi/' /etc/lightdm/lightdm.conf
sed -i 's/#autologin-user-timeout=0/autologin-user-timeout=0/' /etc/lightdm/lightdm.conf

if [ ! -e /home/pi/.config/lxsession/autostart ]
then
	mkdir -p /home/pi/.config/lxsession/autostart
	mkdir -p /home/pi/.config/lxsession/LXDE
	echo "@xscreensaver -no-splash
@~/mplayer-slave" >/home/pi/.config/lxsession/LXDE/autostart
fi

echo "[Desktop Entry]
Type=Application
Exec=/home/pi/mplayer-slave" >/home/pi/.config/lxsession/autostart/pimusic

# Copy music app
cp -r /vagrant/PiGUI/* /home/pi
cp -r /vagrant/PiGUI/.[!.]* /home/pi
mkdir /home/pi/PiMusic
cp -r /vagrant/ignore/music/* /home/pi/PiMusic
cd /home/pi/.config/lxsession
chown -R pi:pi /home/pi

init 6
