
import pickle
import numpy as np
import matplotlib.pyplot as plt
import argparse

from event import Event, Pulse


print("Starting analysis")

import sys
def function_name(filestoprocess): 
  
  j = []
  
  for input in filestoprocess:
    print "Processing %s" % input
    count = 0
    with open(input,'rb') as afile:
      events = pickle.load(afile)
      for event in events:
        for pulse in eventy.pulses:
          if pulse.edge == 0:
            count += 1
      i = (input,count)
      j.append(i)
    return j
function_name(sys.argv[1:])

print(j)


# # open the file
# ifile = open(args.in_file, 'rb')
# events= pickle.load(ifile)
# n_events= len(events)

# print("Read {} events from file".format(n_events))

# # example event loop
# count = [0, 0, 0, 0]  # counts per channel

# for event in events:
#     for pulse in event.pulses:
#         # only count rising edges
#         if pulse.edge == 0:
#             count[pulse.chan] += 1

