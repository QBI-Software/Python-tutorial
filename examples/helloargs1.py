# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 13:53:31 2017

@author: uqecoop2
"""
import sys

def hello(name):
  """Print "Hello " and a name and return None"""
  print("Hello", name)
  
def valid(name):
    # Provide a validity check to ensure bad stuff is not passed in
    return (type(randomname) == str)


# main program starts here
if __name__ == '__main__':
    randomname = None           #ensure that this variable is clean to start
    if (len(sys.argv) > 1):     #test whether any arguments have been passed in
        randomname = sys.argv[1]
    # Check that name is a valid string
    if (randomname is not None and valid(randomname)):
        hello(randomname)
    else:
        print("No name passed in")

