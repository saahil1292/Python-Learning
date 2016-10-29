#!/usr/bin/python2.7

def is_leap(year):
    
    leap = False
    
    if(leap % 4 == 0):
        if (leap % 100 == 0):
            if (leap % 400 == 0):
                leap = True
                    
    return leap

year = int(raw_input())
print is_leap(year)


