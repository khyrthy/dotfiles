#!/bin/bash

echo "Updating dotfiles..."

# Oh My Zsh
figlet Oh My Zsh
sleep 0.2

rm -v ./.zshrc

cp -v ~/.zshrc .

# Qtile
figlet Qtile
sleep 0.2

mkdir -pv ./.config/qtile

rm -v ./.config/qtile/autostart.sh
rm -v ./.config/qtile/rofi-power-menu
rm -v ./.config/qtile/config.py
rm -v ./.config/qtile/screenlayout.sh
rm -v ./.config/qtile/scrnsht-wdw.sh
rm -v ./.config/qtile/scrnsht.sh

cp -v ~/.config/qtile/config.py ./.config/qtile
cp -v ~/.config/qtile/autostart.sh ./.config/qtile
cp -v ~/.config/qtile/rofi-power-menu ./.config/qtile
cp -v ~/.config/qtile/screenlayout.sh ./.config/qtile
cp -v ~/.config/qtile/scrnsht.sh ./.config/qtile
cp -v ~/.config/qtile/scrnsht-wdw.sh ./.config/qtile

# Cava
figlet Cava
sleep 0.2

mkdir -pv ./.config/cava

rm -v ./.config/cava/config
cp -v ~/.config/cava/config ./.config/cava

# Termite
figlet Termite
sleep 0.2

mkdir -pv ./.config/termite

rm -v ./.config/termite/config
cp -v ~/.config/termite/config ./.config/termite

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

