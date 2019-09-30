#!/bin/sh


for I in $(seq 1961 2011)
do
    echo $I
#   python draw_worldmap_famineCountry.py $I
    python draw_worldmap_urbanPopulation.py $I
done
