# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas
import argparse
from os import sep, listdir

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Read CSV Files',
                                         description='''\
                Reads a directory and extracts first cell from each file
    
                 ''')
    parser.add_argument('--filedir', action='store', help='Directory containing files', default="data")
    
    args = parser.parse_args()
    inputdir = args.filedir
    
       
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
    