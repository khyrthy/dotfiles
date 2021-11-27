#!/bin/bash

xfce4-screenshooter --region --save /dev/stdout | xclip -i -selection clipboard -t image/png
