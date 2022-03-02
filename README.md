
# Plotting Codes
These are some basic plotting codes to produce plots of structural analyses. They are
1. OneToOnePlotGen.py
    This code is meant for datasets that have discrete x-axes, i.e. datasets where the x value can be represented by a list of integers.
2. BinPlotGen.py
   This code is meant for datasets that have continuous x-axes, i.e. datasets where the x value is represented by real numbers.

## Important note
These codes can be run as a standalone set of codes but fit into a larger pipeline. These codes are part of the CRISP pipeline. 

## Steps to run
Make sure that the python environment has the `matplotlib` library.
Run `run.binplot.test.sh` and `run.onetoone.test.sh` and compare the output with the valid cases in the /test/test_results directory.


