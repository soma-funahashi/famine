#!/bin/sh
for I in $(seq 2020 2031)
do
    echo $I
#   python draw_worldmap_famineCountry.py $I
    python draw_worldmap_out.py $I
done
