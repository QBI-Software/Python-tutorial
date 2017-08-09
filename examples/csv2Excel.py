# -*- coding: utf-8 -*-
"""
Utility script: csv2Excel
Reads a directory and combines csv files into an excel file
run from console/terminal with (example):
    
>python csv2Excel.py --filedir "data" --output "output.xlsx"

Created on Thu Mar 2 2017

@author: Liz Cooper-Williams, QBI
"""

import argparse
import glob
from os import sep, listdir, R_OK, access
from os.path import join, basename, splitext

import pandas

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Combine CSV files to an Excel file',
                                     description='''\
            Reads a directory and combines csv files into an excel file

             ''')
    parser.add_argument('--filedir', action='store', help='Directory containing files', default="data")
    parser.add_argument('--output', action='store', help='Output file name', default="output.xlsx")

    args = parser.parse_args()

    inputdir = args.filedir
    outputfile = args.filedir + sep + args.output

    print("Input directory:", inputdir)
    if access(inputdir, R_OK):
        seriespattern = '*.csv'
        writer = pandas.ExcelWriter(outputfile, engine='xlsxwriter')
        try:
            files = glob.glob(join(inputdir, seriespattern))
            print("Files:", len(files))
            for f2 in files:
                print(f2)
                (fsheet, _) = splitext(basename(f2))
                data = pandas.read_csv(f2)
                if (not data.empty):
                    data.to_excel(writer, sheet_name=fsheet)
            print("Files combined to: ", outputfile)

        except ValueError as e:
            print("ERROR: ", e)

        except OSError as e:
            print("ERROR: Unable to find or access file:", e)
            pass
        finally:
            writer.save()
            writer.close()
    else:
        print("Cannot access directory: ", inputdir)