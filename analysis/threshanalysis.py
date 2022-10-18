import sys
print(sys.version)
import os
import pickle
import numpy as np
import matplotlib.pyplot as plt
import argparse

from event import Event, Pulse


thresholds=["100","200","300","400","500","600","700","800","900","1000"]
threshs = [int(x) for x in thresholds]
channel_tube_dict={"pmt1":3,
                   "pmt2":3,
		   "pmt3":2,
		   "pmt4":2,
		   "pmt5":1,
		   "pmt6":1,
		   "pmt7":0,
		   "pmt8":0}

for tube in channel_tube_dict.keys():
	counts=[]

    	for thres in thresholds:
        	filename="thresh%s%s.pkl"%(thres,tube)
        	ifile = open(filename, 'rb')
        	events = pickle.load(ifile)
        	count=0
        	for event in events:
            	for pulse in event.pulses:
                	# only count rising edges
                	if pulse.edge == 0:
                    		count+=1
        	counts.append(count)

    	
	plt.plot(threshs,counts, label=tube)
	

plt.xlabel("Threshhold mV")
plt.ylabel("Counts")

plt.legend()

plt.show()
     

