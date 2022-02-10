# Creator: Goutham Mittadhoddo (gm7ps)
# This file plots all output data files in an input directory to linegraphs of histograms.
# Then, it saves the histograms to a specified output directory.
# ...borrowed a lot from Chris' and Robert's code

'''
Invoke the program like this:
python PROGRAM_NAME.py input_file output_file xCol yCol title xlabel ylabel
'''

import sys
import time
import math
import matplotlib.pyplot as plt
import os
import argparse
import numpy as np
import pandas as pd

parser = argparse.ArgumentParser()

begintime = time.time()
### -----------------------------
### Start program.
if (len(sys.argv) != 9):
    print("Error. Incorrect usage.")
    print(
        "usage: python PROGRAM_NAME.py input_file output_file xCol yCol delimiter title xlabel ylabel"
    )
    print("Halt.")
    quit()

begintime = time.time()


### Command line arguments.
input_file = sys.argv[1]
output_file = sys.argv[2]
xCol = int(sys.argv[3])
yCol = int(sys.argv[4])
delimiter = sys.argv[5]
title = sys.argv[6]
xlabel = sys.argv[7]
ylabel = sys.argv[8]

### Echo inputs:

print("=========================")
print("Echo inputs:")
print("the input: ", input_file)
print("the output: ", output_file)

print("=========================")
print("Here is the target file:")
print(input_file)


### Open file.
fh = open(input_file, "r")

# initialize the data and bins
x = []
y = []

## ---------------------
## Read data.
while (True):
    line = fh.readline()
    ### print "line: ",line
    if not line:
        break
    lineStrip = line.strip()
    if len(lineStrip) == 0:
        continue
    if lineStrip[0] == "#":
        continue

    listTokens = line.split(delimiter)
    x.append(float(listTokens[xCol]))

avg_perc=1/len(x)
num_nodes=len(x)
y = np.full(num_nodes,avg_perc)
x_min = min(x)
x_max = max(x)
num_bins = 40
step_size = (x_max-x_min)/(num_bins)

even_spaces = np.linspace(x_min,x_max,(num_bins+1))
xvals=[]
x_index=0
while x_index < len(even_spaces)-1:
    xvals.append((even_spaces[x_index]+even_spaces[x_index+1])/2)
    x_index+=1
    
print("Xmin", x_min)
print("Xmax", x_max)
print("stepSize", step_size)
print("Len xvals",len(xvals))


yvals=buckets = [0] * num_bins

print("Len yvals", len(yvals))

index=0
for value in x:
    raw_pos =((value-x_min)/step_size)
    if raw_pos%1==0:
        index=int(raw_pos-1)
    else:
        index=math.trunc(raw_pos)
    yvals[index]+=avg_perc

fig, ax = plt.subplots()

ax.set_title(title, fontsize="30")
ax.plot(xvals, yvals)
ax.tick_params(axis='x', labelsize=25)
ax.tick_params(axis='y', labelsize=25)
ax.set_xlabel(xlabel, fontsize=25)
ax.set_ylabel(ylabel, fontsize=25)

plt.savefig(output_file+'.png', bbox_inches='tight')

fig2, ax2 = plt.subplots()

ax2.set_title("Log Scale of "+title, fontsize="30")
ax2.plot(xvals, yvals)
ax2.tick_params(axis='x', labelsize=25)
ax2.tick_params(axis='y', labelsize=25)
ax2.set_yscale('log')
ax2.set_xlabel(xlabel, fontsize=25)
ax2.set_ylabel(ylabel, fontsize=25)

plt.savefig(output_file+'.log.png', bbox_inches='tight')



endtime = time.time()
print("=========================")
print("Running time, start to finish: {sec} (s), {hr} (hr): ".format(
    sec=round(endtime - begintime, 3),
    hr=round(float(endtime - begintime) / 3600.0, 3)))

print("good termination")

