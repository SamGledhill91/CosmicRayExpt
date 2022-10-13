#!/bin/sh

for j in 200 225 250 275 300 325 350 375 400 425 450 475 500 525 550 575 600; do
  acquire.py -t 100 -o thresh$jpmt1.pkl -0 $j -1 $j -2 $j -3 -e 0x8 
  acquire.py -t 100 -o thresh$jpmt2.pkl -0 $j -1 $j -2 $j -3 -e 0x4
  acquire.py -t 100 -o thresh$jpmt3.pkl -0 $j -1 $j -2 $j -3 -e 0x2
  acquire.py -t 100 -o thresh$jpmt4.pkl -0 $j -1 $j -2 $j -3 -e 0x1
done
