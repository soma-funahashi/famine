#!/bin/sh

cd ../../fig/outf/
convert -layers optimize -loop 0 -delay 30 future_ssp1_*.png -delay 240 Last.png anim.gif
