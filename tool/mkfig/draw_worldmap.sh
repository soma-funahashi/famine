#!/bin/sh
###########################################################
#to          : draw a map of input data of each year
#by          : Soma Funahashi, U-Tokyo, IIS
#last update : 2019/10/15
###########################################################

for I in $(seq 1961 2012)
do
    echo $I
#   python draw_worldmap_famineCountry.py $I
    python draw_worldmap_out.py $I
done
