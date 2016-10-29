#!/usr/bin/python2.7

from urllib import urlopen
import re, time

uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
nothing_rep = "and the next nothing is (\d+)"
nothing = "8022"
nothing_rep_1 = "Yes. Divide by two and keep going."


while True:
    try:
	source = urlopen(uri % nothing).read()
	nothing = re.search(nothing_rep, source).group(1)
	'''if not source:
	    nothing = int(nothing) // 2'''
    except:
	break

    print nothing
