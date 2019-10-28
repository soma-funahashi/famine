#!/bin/sh
###########################################################
#to          : draw a gif animation of model output
#by          : Soma Funahashi, U-Tokyo, IIS
#last update : 2019/10/15
###########################################################

cd ../fig/famineCountry
convert -layers optimize -loop 0 -delay 30 famineCountry*.png -delay 240 Last.png anim.gif
