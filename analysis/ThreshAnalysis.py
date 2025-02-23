import sys
print(sys.version)
import os
import pickle
# import numpy as np
# import matplotlib.pyplot as plt
import argparse

from event import Event, Pulse

pathToFiles = '/home/ph18493/data/threshcali'
threshIncrement =  100

matrix

for filename in os.listdir(pathToFiles):
    f = os.path.join(pathToFiles, filename)
    if os.path.isfile(f):
        print(filename.replace('thresh', '').replace('pmt', ',').replace('.pkl', ''))
        ifile = open(f, 'rb')
        events = pickle.load(ifile)
        n_events= len(events)
        
        print("Read {} events from file".format(n_events))
        
        # example event loop
        count = [0, 0, 0, 0]  # counts per channel
        
        for event in events:
            for pulse in event.pulses:
                # only count rising edges
                if pulse.edge == 0:
                    count[pulse.chan] += 1
        x = filename.replace('thresh', '').replace('pmt', ',').replace('.pkl', '')
        x.split(",")
        x = [int(i) for i in x]
        x.append(count[pulse.chan])
        
        matrix.append(x)
        
print(matrix)        
        print("Counts by channel")
        print("Channel 0 : {} ".format(count[0]))
        print("Channel 1 : {} ".format(count[1]))
        print("Channel 2 : {} ".format(count[2]))
        print("Channel 3 : {} ".format(count[3]))
        
        # # now find concidences betwen two channels (0 and 1)
        # n_coinc = 0
        # for event in events:
        #     found0 = False
        #     found1 = False
        #     for pulse in event.pulses:
        #         # only count rising edges
        #         if pulse.edge==0 and pulse.chan == 0:
        #             found0 = True
        #         if pulse.edge==0 and pulse.chan == 1:
        #             found1 = True
        #     if found0 and found1:
        #         n_coinc += 1
                    
        # print("N (0,1) coincidences : {}".format(n_coinc))
        
        # # get some pulse time information
        # dts = []
        # for event in events:
        #     found0 = False
        #     found1 = False
        #     time0 = 0.
        #     time1 = 0.
        #     for pulse in event.pulses:
        #         # only count rising edges
        #         if pulse.edge==0 and pulse.chan == 0:
        #             found0 = True
        #             time0 = pulse.time
        #         if pulse.edge==0 and pulse.chan == 1:
        #             found1 = True
        #             time1 = pulse.time
        #     if found0 and found1:
        #         dts.append(abs(time1-time0))
        
        # # print some summary info
        # print("Mean delta-t : {}".format(np.mean(dts)))
        # print("Std dev delta-t : {}".format(np.std(dts)))
        
        # bins = np.linspace(0.,2000., 100)
        # plt.hist(dts, bins)
        # plt.yscale('log')
        # plt.ylabel("N")
        # plt.xlabel(r'$\Delta t$')
        # plt.show()
