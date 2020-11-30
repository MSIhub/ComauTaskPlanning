# ComauTaskPlanning #
This repository contains the library functions for task planning and data recording for Comau serial robot

## 0. PRE-PREQUISITE ##
 - Clone this GitHub Repository
 - Copy the python file main_example1.py and rename it to your choice in the same directory

## 1. DESIGN TRAJECTORY ##
 - Decide the behaviour of the trajectory (If possible, try to split it into lines and circle combo)
 - Write the equation of the traj in python
 - in the python script copied, replace the trajectory part with the equation of the designed trajctory

## 2. CREATE PDL Files ##
 - This also should be done in the same script
 - Just change the "pname" to the program name you prefer. Avoid repeating same program name as it will delete the previous one
 - Modify the following parameter if necessary: lin_spd, rot_spd and tool_frame_offset
 - Execute the python file with the required packages installed.
 - This execution will create a folder "\ToRobot" under current directory and then creates another folder "toRobot\pname". You will find two pdl files one for motion feedback TCP server and another for the motion program.
 
 ## 3. PREPARING COMAU ROBOT ##
 - Open WinC4G application(Comau's application)
 - Navigate to the folder where the two created pdl files are located
 - translate both the pdl files to .cod files without any error 
 (* Translation of pdl to cod will not happen if the robot is connected)
 - Connect to the robot with username and pass (pu, pu)
 - Navigate to TD: (temporary folder, all the files will be erased upon robot shutdown)
 - Copy the two cod files in there
 - Go to the terminal in WinC4G app.
 - Press the button F6, F6 and F4 in the same order
 - type TD:\(pname).cod (You should be able to see START the teaching pendant info )
 - type TD:\motion_feedback.cod (You should be able to see "######motion feedback program initiated...")
 
 >NOTE:
 >> Do not start the client server before the motion_feedback.cod is running (server must be started for the client to listen)
 >>> Do not press the teaching pendant start without starting the client server

 ## 4. RUNNING THE TRAJ AND RECORDING DATA ##
 - All need to be done now is press "START" in teaching pendant
 - First, the robot will move to the starting position of the trajectory and then start the motion trajectory while triggering motion_feedback to the file in PC
 - Data will stop recording as soon as the motion of robot is stopped.
 - As of now, you have the raw data of the trajectory that the robot followed.
  
