#!/usr/bin/env python

# data analysis example program
# Including some examples of how to use DataFrames from pandas
#
# Usage :
# python analysis.py -i test.dat

import pickle
import numpy as np
import matplotlib.pyplot as plt
import argparse
import math

from event import Event, Pulse

parser = argparse.ArgumentParser(description='Analyse CSV file')
parser.add_argument("-i", "--in_file", help="input file")
parser.add_argument("-o", "--out_file", help='output file')
parser.add_argument("-n", "--n_max", help='max number of lines to process')

args = parser.parse_args()

print("Starting analysis")

# open the file
ifile = open(args.in_file, 'rb')
events= pickle.load(ifile)
n_events= len(events)

print("Read {} events from file".format(n_events))

# example event loop
count = [0, 0, 0, 0]  # counts per channel

for event in events:
    for pulse in event.pulses:
        # only count rising edges
        if pulse.edge == 0:
            count[pulse.chan] += 1

print("Counts by channel")
print("Channel 0 : {} ".format(count[0]))
print("Channel 1 : {} ".format(count[1]))
print("Channel 2 : {} ".format(count[2]))
print("Channel 3 : {} ".format(count[3]))

# now find concidences betwen two channels (0 and 1)


cominations = []

n_coinc01 = n_coinc02 = n_coinc03 = n_coinc12 = n_coinc13 = n_coinc23 = 0
n_coinc012 = n_coinc013 = n_coinc021 = n_coinc023 = n_coinc031 = n_coinc032 = n_coinc120 = n_coinc123 = n_coinc130 = n_coinc132 = n_coinc230 = n_coinc231 = 0
for event in events:
    found0 = False
    found1 = False
    found2 = False
    found3 = False
    for pulse in event.pulses:
        # only count rising edges
        if pulse.edge==0 and pulse.chan == 0:
            found0 = True
        if pulse.edge==0 and pulse.chan == 1:
            found1 = True
        if pulse.edge==0 and pulse.chan == 2:
            found2 = True
        if pulse.edge==0 and pulse.chan == 3:
            found3 = True
    if found0 and found1:
        n_coinc01 += 1.
	if found2:
		n_coinc012 +=1.
	if found3:
		n_coinc013 +=1.
    if found0 and found2:
        n_coinc02 += 1.
	if found1:
		n_coinc021 +=1.
	if found3:
		n_coinc023 +=1.
    if found0 and found3:
        n_coinc03 += 1.
	if found2:
		n_coinc032 +=1.
	if found1:
		n_coinc031 +=1.
    if found1 and found2:
        n_coinc12 += 1.
	if found0:
		n_coinc120 +=1.
	if found3:
		n_coinc123 +=1.
    if found1 and found3:
        n_coinc13 += 1.
	if found0:
		n_coinc130 +=1.
	if found2:
		n_coinc132 +=1.
    if found2 and found3:
        n_coinc23 += 1.
	if found0:
		n_coinc230 +=1.
	if found1:
		n_coinc231 +=1.

P2g01 = n_coinc012/n_coinc01
P2g03 = n_coinc032/n_coinc03
P2g13 = n_coinc132/n_coinc13
P0g12 = n_coinc120/n_coinc12
P0g13 = n_coinc130/n_coinc13
P0g23 = n_coinc230/n_coinc23
P1g02 = n_coinc021/n_coinc02
P1g03 = n_coinc031/n_coinc03
P1g23 = n_coinc231/n_coinc23
P3g01 = n_coinc013/n_coinc01
P3g02 = n_coinc023/n_coinc02
P3g12 = n_coinc123/n_coinc12

erP2g01 = math.sqrt((P2g01*(1-P2g01))/n_coinc01)
erP2g03 = math.sqrt((P2g03*(1-P2g03))/n_coinc03)
erP2g13 = math.sqrt((P2g13*(1-P2g13))/n_coinc13)
erP0g12 = math.sqrt((P0g12*(1-P0g12))/n_coinc12)
erP0g13 = math.sqrt((P0g13*(1-P0g13))/n_coinc13)
erP0g23 = math.sqrt((P0g23*(1-P0g23))/n_coinc23)
erP1g02 = math.sqrt((P1g02*(1-P1g02))/n_coinc02)
erP1g03 = math.sqrt((P1g03*(1-P1g03))/n_coinc03)
erP1g23 = math.sqrt((P1g23*(1-P1g23))/n_coinc23)
erP3g01 = math.sqrt((P3g01*(1-P3g01))/n_coinc01)
erP3g02 = math.sqrt((P3g02*(1-P3g02))/n_coinc02)
erP3g12 = math.sqrt((P3g12*(1-P3g12))/n_coinc12)

probabilities = {"P2g01": P2g01,
		"P2g03": P2g03,
		"P2g13": P2g13,
		"P0g12": P0g12,
		"P0g13": P0g13,
		"P0g23": P0g23,
		"P1g02": P1g02,
		"P1g03": P1g03,
		"P1g23": P1g23,
		"P3g01": P3g01,
		"P3g02": P3g02,	
		"P3g12": P3g12}
errors = [erP2g01,erP2g03,erP2g13,erP0g12, erP0g13,erP0g23,erP1g02,erP1g03,erP1g23,erP3g01,erP3g02,erP3g12]


            
print("N (0,1) coincidences : {}".format(n_coinc01))
print("N (0,2) coincidences : {}".format(n_coinc02))
print("N (0,3) coincidences : {}".format(n_coinc03))
print("N (1,2) coincidences : {}".format(n_coinc12))
print("N (1,3) coincidences : {}".format(n_coinc13))
print("N (2,3) coincidences : {}".format(n_coinc23))

for i in range(12):
	name = probabilities.keys()[i]
	probability = probabilities[name]
	error = errors[i]
	print("{}={} with error = {}".format(name, probability,error))

# get some pulse time information
dts = []
for event in events:
    found0 = False
    found1 = False
    time0 = 0.
    time1 = 0.
    for pulse in event.pulses:
        # only count rising edges
        if pulse.edge==0 and pulse.chan == 0:
            found0 = True
            time0 = pulse.time
        if pulse.edge==0 and pulse.chan == 1:
            found1 = True
            time1 = pulse.time
    if found0 and found1:
        dts.append(abs(time1-time0))

# print some summary info
print("Mean delta-t : {}".format(np.mean(dts)))
print("Std dev delta-t : {}".format(np.std(dts)))

bins = np.linspace(0.,2000., 100)
plt.hist(dts, bins)
plt.yscale('log')
plt.ylabel("N")
plt.xlabel(r'$\Delta t$')
plt.show()
