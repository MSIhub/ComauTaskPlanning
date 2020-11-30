# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:02:06 2019

Last edited on Fri Jan 3 11:50:50 2020

@author: Sadiq

Example file to use the PdlFileGen_lib library to create task level programming of trajectory for COMAU Robot WinC4G
# Testing template for comau motion programming

"""


import sys
import numpy as np
sys.path.insert(0, r'F:/ViveDynTrackTest/PythonWorkspace/lib')
import PdlFileGen_lib as pfg

np.set_printoptions(precision=8)

# Trajectory behavior
num_of_points = 2 #n=n-1
A = [0, -500, 1500, 0, 0, 0]
B = [1000, -500, 1500, 0, 0, 0]
traj_data = list(pfg.get_equidistant_points(A,B,num_of_points))

# ENTER THE PROGRAM NAME
pname = "unitTest1"

# Writing to a txt file
pfg.write_file(pname, traj_data)

# Loading the trajectory file
data = pfg.load_traj_file(pname)

# Generate motion program PDL file
lin_spd = 1 #m/s
rot_spd = 1 #rad/s
tool_frame_offset = [0, 0, 0, 0, 0, 0 ] # Tool frame offset, assuming no tool is present
pfg.gen_pdl_file(pname, data, lin_spd, rot_spd, "mf",tool_frame_offset) # "mf" for tcp connection

# Moving the files that need to be copied into robot into a folder with the name of the program
# for TCP IP connection data extraction #Sampling rate will vary, should resample while post proccesing, Matlab scripts available for post processing
pfg.move_files_Net(pname)

#########################################################################################
############### Sample scripts #########################################################
# Creating list of lists for writing in file
#traj_data = []
#for n in range(0, (len(x)-1)):
#    temp_data = list([x[n], y[n], z[n], a[n], e[n], r[n]])
#    traj_data.append(temp_data)

# Generate motion feedback pdl thread and txt file to store data
#sampling_rate = 100 # in Hz
#pfg.gen_motion_feedback_file(pname, sampling_rate)
#pfg.move_files_reqforrobot(pname) # for text file in TD: folder of robot
