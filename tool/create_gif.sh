#!/bin/sh

cd ../fig/famineCountry
convert -layers optimize -loop 0 -delay 30 famineCountry*.png -delay 240 Last.png anim.gif
