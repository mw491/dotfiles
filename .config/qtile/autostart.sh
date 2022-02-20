#!/bin/bash
##### AUTOSTART PROGRAMS FOR QTILE #####

picom --config $HOME/.config/picom/picom.conf & # compositer for transparency
volumeicon & # change volume
nm-applet & # wifi management
pamac-tray & # pamac tray for updates
nitrogen --restore # wallpaper
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & # password authenticator
/usr/lib/xfce4/notifyd/xfce4-notifyd & #notifcations
xfce4-power-manager & # sleep on idle
