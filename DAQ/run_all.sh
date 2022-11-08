#!/bin/sh

# example script for automating several data taking runs
# Usage :
#  bash run_all.sh
#

acquire.py -t 3600 -c 3 -o 1hrcoinc1458.txt -0 300 -1 400 -2 400 -3 275 -e 0xF -s ~/code/CosmicRayExpt/DAQ/daq.cfg 
acquire.py -t 3600 -c 2 -o 1hrcoinc458.txt -0 300 -1 400 -2 400 -3 275 -e 0x7 -s ~/code/CosmicRayExpt/DAQ/daq.cfg
acquire.py -t 3600 -c 2 -o 1hrcoinc158.txt -0 300 -1 400 -2 400 -3 275 -e 0xB -s ~/code/CosmicRayExpt/DAQ/daq.cfg
acquire.py -t 3600 -c 2 -o 1hrcoinc148.txt -0 300 -1 400 -2 400 -3 275 -e 0xD -s ~/code/CosmicRayExpt/DAQ/daq.cfg
acquire.py -t 3600 -c 2 -o 1hrcoinc145.txt -0 300 -1 400 -2 400 -3 275 -e 0xE -s ~/code/CosmicRayExpt/DAQ/daq.cfg
acquire.py -t 36000 -c 3 -o 10hrcoinc1458.txt -0 300 -1 400 -2 400 -3 275 -e 0xF -s ~/code/CosmicRayExpt/DAQ/daq.cfg 
