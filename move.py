#!/usr/bin/python

#Script to move all your folders (No other files) from one location to another
import os, shutil

path = '/home/sharmas/Desktop/'
path2 = '/home/sharmas/Saahil/others/'

# This will create a list with the paths of the folder.
#os.path.isdir checks if the input is a directory or not 
dir = [os.path.join(path,f) for f in os.listdir(path) if os.path.isdir(os.path.join(path,f))]

for i in dir:
    shutil.move(i, path2) #It is the closest function to the 'mv' command of linux 

