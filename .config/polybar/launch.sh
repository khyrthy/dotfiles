#!/bin/bash

killall polybar

if type "xrandr"; then
	  for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
		      echo $m
		      MONITOR=$m polybar --reload bar &
		        done
		else
			  polybar --reload bar &
fi
