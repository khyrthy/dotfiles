#!/bin/bash

killall polybar
polybar --config=~/.config/polybar/config.ini bar &
polybar --config=~/.config/polybar/config.ini bar2
