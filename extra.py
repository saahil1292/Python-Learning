#!/usr/bin/python2.7

import time
import webbrowser
import random

alarm = raw_input(">")

Time = time.strftime("%H%M%S")

with open("YT") as f:
	content = f.readlines()
		
while alarm!=Time:
	print "Time is " + Time
	Time = time.strftime("%H%M%S")
	time.sleep(1)
		
if(alarm==Time):
	print "Time to Wake Up"
	#webbrowser.open(content)
	print random.choice(content)
