#Created by: Brandon Schurter
#Last updated: Feb. 24, 2017

#Purpose: Plot results from convert_genome script to understand results

import matplotlib.pyplot as plt
import numpy as np
import sh

outputfolder = "/home/ubuntu/workspace/DNAdecode/output/"
#List results in output folder
output_files = sh.ls(outputfolder)
output_files = output_files.split()

data = dict()
for output_file in output_files:
    data['output_file'] = np.genfromtxt(output_file, delimiter=',')
    


