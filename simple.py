#!/usr/bin/python2.7

def test():
	generator = (i for i in range(10))
	
	for element in generator:
		print element
		
		#print len(generator)

test()
