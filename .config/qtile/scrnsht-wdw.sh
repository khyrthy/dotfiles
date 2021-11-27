#!/bin/bash

xfce4-screenshooter --window --save /dev/stdout | xclip -i -selection clipboard -t image/png
