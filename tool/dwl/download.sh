#!/bin/sh
###########################################################
#to          : downloading data from server
#by          : Soma Funahashi, U-Tokyo, IIS
#last update : 2019/10/30
###########################################################

FILE=$1
PORT="soma@rainbow.iis.u-tokyo.ac.jp"
H08DIR="/work/a01/soma/H08_20190701/fig/"
FAMDIR="/Users/SomaFunahashi/Documents/Oki_lab/Master/famine/dat/sow/"

scp $PORT:$H08DIR$FILE $FAMDIR
