---
title: Handling Errors
teaching: 30
exercises: 30
questions:
- "How can I write Python programs that don't stop when they get an error?"
objectives:
- "Understanding what an error is"
- "Catching errors"
- "Throwing errors"
- "Recording errors but continuing the program"
- "Cross-platform tips with Files"
keypoints:
- "A syntax error is often just a typo, but can also be incorrectly named methods or incorrect arguments passed into a method"
- "File errors are very common but can be managed with some basic checks"
- "Catching errors can allow them to be noted but the program can still run"
- "Safely exiting a program if an error is encountered is always the best thing to do"
---
# Handling Errors in Python
So we have scripts which run just fine as long as the information we give them is what they expect.  Errors appear when the script/program encounters conditions it does not know how to handle.  This is not as scary as it sounds and it is very nice to have scripts which you can feel confident are not going to "crash" as soon as someone else tries to use them.  

## What can go wrong?
Running your script on your own system may be working perfectly but is it also going to work on another system?

A brief list of what can commonly go wrong:

1. Syntax errors such as typos or incorrect arguments
1. Files needed by the script can't be found or accessed
1. A list created dynamically may not get created at all or items in the list expected at a certain index (location) are missing
1. Values passed in as arguments may not be what was expected by the script

## Syntax errors
As you create your script, it is very common to have *syntax* errors, that is, typos, incorrectly named methods or passing in the wrong number of arguments to a method.  Catching these early is easier with an editor like **Spyder**.
1. Run the following code and see the error - also note how Spyder highlights the problem.

```python
if (1 == 1)
    print("This is a syntax error")
```
You should see an output showing that something is missing (what should this be?):
~~~
if (1 == 1)
               ^
SyntaxError: invalid syntax
~~~


## Catching errors
Fortunately, we can catch these errors and then do something about them before they abruptly end our program.
The structure is a "try-except-finally" block of code which is wrapped around your code.

```python
try:
  prnt("This is a name error")  #misspelt print so no method found
except NameError as e:
  print("Caught this error:", e)
finally:
  print("I'm always going to run this bit")

```

>The `finally` section is optional

### "Continue anyway" errors
When running in a loop and the error is **minor**, such as the first line in a text file is blank and you just want to skip it, use `continue` in the `except` block to tell the program to go to the next instruction.

### "Stop running if this occurs" errors
When running in a loop and the error is **major** and you cannot continue without the information:
1. use `break` and the loop will end
1. use `pass` and the program will pass to the next instruction
1. only use `exit(0)` if you really want to terminate everything (in Spyder, this also shuts down the python kernel)

## Reading Files
So, we will see how to put this in a script which reads the gapminder data as we have done in previous lessons.
Files can be missing or not accessible so we will include error catching to notify us of these problems.

Previously:
```python
import pandas

data = pandas.read_csv('data/gapminder_gdp_oceania.csv')
print(data)
```

1. We will change the hard-coded filename to variables
1. We will also use a library variable called `os.sep` which separates filenames according to operating system so this code can be run on Mac, Unix or Windows

```python
filename = datadir + os.sep + fname
data = pandas.read_csv(filename)
print(data)
```

1. Now put the code in a `try:` block

```python
import pandas
from os import sep

inputdir = "data"
fname = "gapminder_gdp_oceania.csv"

try:
    filename = inputdir + sep + fname
    data = pandas.read_csv(filename)
    if (not data.empty):
       print(data.iloc[0, 0])

except OSError as e:
    print("ERROR: Unable to find or access file:", e)
    pass

```
## Looping through a directory
Often, you will be using a Python script to read files in a directory.

1. We will add a loop for our files:

```python
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
```
## Making a dynamic script
Finally, we will allow the directory to be loaded from outside the script.

1. Now we will incorporate our **argument parser** from the previous lesson so the directory can be specified when we run the script rather than having to change the code
1. Don't forget the special line `if __name__ == '__main__':` so we can run from the terminal console

```python
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

```

#### Challenge
Take this one step further and put your code into methods.

#### Challenge
Combine all our csv files into an excel file


```python
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
```
