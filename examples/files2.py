# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas
from os import sep, listdir

inputdir = "data"
   
try:
    for fname in listdir(inputdir):
        print(fname)
        filename = inputdir + sep + fname
        data = pandas.read_csv(filename)
        if (not data.empty):
           print(data.iloc[0, 0])

except OSError as e:
    print("ERROR: Unable to find or access file:", e)
    pass
    