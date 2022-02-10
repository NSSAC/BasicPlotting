# Creator: Goutham Mittadhoddo (gm7ps)
# This file plots data from a file that plots discrete x values where each x can be plotted to one y. 
# Counterexample of this would be where the x axis is continuous and there need to be bins.
# ...borrowed a lot from Chris' and Robert's code

'''
Invoke the program like this:
python PROGRAM_NAME.py input_file output_file xCol yCol title xlabel ylabel
'''

import sys
import time
import matplotlib.pyplot as plt
import argparse
import pandas as pd

parser = argparse.ArgumentParser()

begintime = time.time()
### -----------------------------
### Start program.
if (len(sys.argv) != 8):
    print("Error. Incorrect usage.")
    print(
        "usage: python PROGRAM_NAME.py input_file output_file xCol yCol title xlabel ylabel"
    )
    print("Halt.")
    quit()

begintime = time.time()


### Command line arguments.
input_file = sys.argv[1]
output_file = sys.argv[2]
xCol = int(sys.argv[3])
yCol= int(sys.argv[4])
title = sys.argv[5]
xlabel = sys.argv[6]
ylabel = sys.argv[7]

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

data = pd.read_csv(input_file, sep=" ", header=None)
# initialize the data and bins
x = data[xCol]
y = data[yCol]
fig, ax = plt.subplots()

ax.set_title(title, fontsize="30")
ax.scatter(x, y, color="blue", marker="*")
ax.tick_params(axis='x', labelsize=25)
ax.tick_params(axis='y', labelsize=25)
ax.set_xlabel(xlabel, fontsize=25)
ax.set_ylabel(ylabel, fontsize=25)

plt.savefig(output_file+'.png', bbox_inches='tight')

fig2, ax2 = plt.subplots()

ax2.set_title("Log Scale of "+title, fontsize="30")
ax2.scatter(x, y, color="blue", marker="*")
ax2.tick_params(axis='x', labelsize=25)
ax2.tick_params(axis='y', labelsize=25)
ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.set_xlabel(xlabel, fontsize=25)
ax2.set_ylabel(ylabel, fontsize=25)

plt.savefig(output_file+'.log.png', bbox_inches='tight')
    


endtime = time.time()
print("=========================")
print("Running time, start to finish: {sec} (s), {hr} (hr): ".format(
    sec=round(endtime - begintime, 3),
    hr=round(float(endtime - begintime) / 3600.0, 3)))

print("----------------------good termination----------------------")

