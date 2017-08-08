# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 13:53:31 2017

@author: uqecoop2
"""
import math

def helloworld():
    """Print "Hello World" and return None"""
    print("Hello World")

def hello(name):
  """Print "Hello " and a name and return None"""
  print("Hello", name)
  
def get_pi():
    """Get value of pi"""
    return math.pi

# main program starts here
if __name__ == '__main__':
    helloworld()
    hello("Josephine")
    print('pi is', get_pi())
