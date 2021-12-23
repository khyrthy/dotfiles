#!/bin/bash

echo "Updating dotfiles..."

# Oh My Zsh
figlet Oh My Zsh
sleep 0.2

rm -v ./.zshrc

cp -v ~/.zshrc .

# i3
figlet i3-gaps
sleep 0.2

mkdir -pv ./.config/i3

rm -v ./.config/i3/config
rm -v ./.config/i3/rofi-power-menu
rm -v ./.config/i3/screenlayout.sh

cp -v ~/.config/i3/config ./.config/i3
cp -v ~/.config/i3/rofi-power-menu ./.config/i3
cp -v ~/.config/i3/screenlayout.sh ./.config/i3

# Polybar
figlet Polybar
sleep 0.2

mkdir -pv ./.config/polybar

rm -v ./.config/polybar/launch.sh
rm -v ./.config/polybar/config.ini

cp -v ~/.config/polybar/launch.sh ./.config/polybar
cp -v ~/.config/polybar/config.ini ./.config/polybar

# Cava
figlet Cava
sleep 0.2

mkdir -pv ./.config/cava

rm -v ./.config/cava/config
cp -v ~/.config/cava/config ./.config/cava

# Kitty
figlet Kitty
sleep 0.2

mkdir -pv ./.config/kitty

rm -v ./.config/kitty/kitty.conf

cp -v ~/.config/kitty/kitty.conf ./.config/kitty

# Neovim
figlet neovim
sleep 0.2

mkdir -pv ./.config/nvim

rm -v ./.config/nvim/init.vim
cp -v ~/.config/nvim/init.vim ./.config/nvim

# Ranger
figlet Ranger
sleep 0.2

mkdir -pv ./.config/ranger

rm -v ./.config/ranger/rc.conf
cp -v ~/.config/ranger/rc.conf ./.config/ranger

# Rofi
figlet Rofi
sleep 0.2

mkdir -pv ./.config/rofi

rm -v ./.config/rofi/config.rasi
cp -v ~/.config/rofi/config.rasi ./.config/rofi

# Picom
figlet Picom
sleep 0.2

mkdir -pv ./.config/picom

rm -v ./.config/picom/picom.conf
cp -v ~/.config/picom/picom.conf ./.config/picom

# Dunst
figlet dunst
sleep 0.2

mkdir -pv ./.config/dunst

rm -v ./.config/dunst/dunstrc
cp -v ~/.config/dunst/dunstrc ./.config/dunst

# Browser's homepage
figlet Homepage
sleep 0.2

rm -v ./homepage.html
cp -v ~/Documents/.homepage ./homepage.html

