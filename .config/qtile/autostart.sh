#!/bin/bash

# Policy kit
lxqt-policykit-agent

# Dunst
dunst &

# Set keymap to fr
setxkbmap fr

# Screen configuration
~/.config/qtile/screenlayout.sh


# Launch some programs
nm-applet &
picom &

# Restore wallpaper
feh --bg-fill ~/Images/Wallpapers/wallpaper
