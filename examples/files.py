# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas
from os import sep

inputdir = "data"
fname = "gapminder_gdp_oceania.csv"
   
try:
    filename = inputdir + sep + fname
    data = pandas.read_csv(filename)
    if (not data.empty):
       print(data.describe())

except OSError as e:
    print("ERROR: Unable to find or access file:", e)
    pass
    