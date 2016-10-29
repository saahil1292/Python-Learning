#! usr/bin/python2.7

#importing libraries
import time
import webbrowser
import random

#input the time by user
print "Enter the time"
alarm = raw_input(">")

#specify a format for time
Time = time.strftime("%H%M%S")
	
#when the system time is not equal to the time specified by user
while(alarm!=Time):	
	print "Time is " + Time
	#time is incremented by 1, if kept outside loop, it shows initial time continuosly
	Time = time.strftime("%H%M%S")
	#gives a 1 second pause so that loop doesnt flood with results
	time.sleep(1)

#when the system time is equal to the time specified by user		
if(alarm==Time):
	print "Time to wake up"
	#read the contents of a file
	with open("YT") as f:
		content = f.readlines()
	#reads the contents of the file randomly and store in a variable
	random_vid = random.choice(content)
	#opens the content in browser using webbrowser library
	webbrowser.open(random_vid)
	
