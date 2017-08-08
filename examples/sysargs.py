# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 14:59:04 2017

@author: uqecoop2
"""

import sys
# main program starts here
if __name__ == '__main__':
    program = sys.argv[0]
    print("Program running is:", program)
    #Now check for extra arguments
    if (len(sys.argv) == 3):
        argument1 = sys.argv[1]
        argument2 = sys.argv[2]
        print("Arguments:", argument1, argument2)
