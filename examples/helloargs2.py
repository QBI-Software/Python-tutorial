# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 13:53:31 2017

@author: uqecoop2
"""
import argparse

def hello(name):
  """Print "Hello " and a name and return None"""
  print("Hello", name)
  
def valid(name):
    # Provide a validity check to ensure bad stuff is not passed in
    return (type(randomname) == str)


# main program starts here
if __name__ == '__main__':
    #Setup the argument parser class
    parser = argparse.ArgumentParser(prog='Hello program',
                                     description='''\
            Reads a name and says hello

             ''')
    #We use the optional switch -- otherwise it is mandatory
    parser.add_argument('--randomname', action='store', help='A name', default="Josephine")
    #Run the argument parser
    args = parser.parse_args()
    #Extract our value or default 
    randomname = args.randomname 
    
    # Check that name is a valid string
    if (randomname is not None and valid(randomname)):
        hello(randomname)
    else:
        print("No name passed in")

