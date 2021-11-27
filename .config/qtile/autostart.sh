#!/bin/bash

# Policy kit


# Set keymap to fr
setxkbmap fr

# Screen configuration
~/.config/qtile/screenlayout.sh


# Launch some programs
nm-applet &
picom &

# Restore wallpaper
nitrogen --restore
