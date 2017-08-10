---
title: Writing a script
teaching: 30
exercises: 30
questions:
- "How can I write Python programs that will run as scripts?"
objectives:
- "Using Spyder to develop Python scripts"
- "Organizing code within a script"
- "Allowing flexibility - running with arguments"
- "Using safe methods for arguments"
keypoints:
- "A script is run from top to bottom, with import statements at the top then methods, then instructions"
- "The `sys` library connects a Python program to the system it is running on."
- "The list `sys.argv` contains the command-line arguments that a program was run with."
- "The `arparse` library is the safest way to use command line arguments"
---
# Writing a Script in Python
So far, we have covered the main programming structures used in Python.  We will now put that together in a script which can be run on demand.

## Using **Spyder** which is part of the **Anaconda** suite
Spyder is an application where you can edit and run your Python scripts.  As part of Anaconda, there are a large number of scientific packages which come pre-installed, to make it easier for scientists getting started in programming.  
1. Open **Anaconda Navigator** and launch **Spyder**.

We will run through a brief overview of the panels:
1. Left panel: Editor
  - this is a special type of editor which understands python
  - as you type, possible options may appear to assist you
  - key words are highlighted to help readability and understanding

2. Top Right panel: Help
  - **Variable explorer:** as a program runs, variables are loaded here with their values
  - **File explorer:** list of files in the current working directory
  - **Help:** documentation and tutorials

3. Bottom Right panel: Console
  - **Python console:** standard python command-line (like typing `python` in a terminal window)
  - **IPython console:** interactive python (like Jupyter cells)

## Organizing your code to run as a script
In **Spyder**, a new file is created when you first open the application.  This is called *temp.py*.
1. Create a new project under **Projects** -> **New Project** in your required directory
1. Save the temp file to *hello.py*
1. Type the following (the HelloWorld mantra):

```c
print("Hello World")
```
1. Click on the **green arrow** in the top toolbar.  A popup window may appear which allows you to change a few things.  Accept the defaults and click `OK`
1. Have a look in the IPython console window and you should see the output similar to:
~~~
runfile('D:/Projects/Python-tutorial/examples/hello.py', wdir='D:/Projects/Python-tutorial/examples')
Hello World
~~~

### Methods
Recall that it is useful to group code into **methods** so replace the code with:

```c
def hello():
    """Print "Hello World" and return None"""
    print("Hello World")

# main program starts here
hello()
```
1. Run again as before and the same output will appear in the console window.
1. As we have run the output in the IPython console window and we have defined a method called `hello()`, what will happen if we just type `hello()` in the console?

### Libraries
We will now use a library as we did in previous lessons. Take note of the order.

1. The `import` statement goes at the top
1. The methods should come next but should be before the instructions (main body)
1. The instructions for running the methods go at the end

try this example:
```python
import math

def hello():
    """Print "Hello World" and return None"""
    print("Hello World")

def get_pi():
    """Get value of pi"""
    return math.pi

# main program starts here
hello()
print('pi is', get_pi())
```

>After running this script, you can type `help(math)` in the IPython console - just as we did in Jupyter but it has to be loaded with `import math` first


### External
Before we move on, there is an extra line required when running the script from outside this environment:

```python
if __name__ == '__main__':
```

Insert this line above `hello()` then indent the following code:

```python
# main program starts here
if __name__ == '__main__':
    hello()
    print('pi is', get_pi())
```

This allows us to run from a terminal window:
`python hello.py`


## Flexible code - running with arguments

So how would we make this script more dynamic?

We will change the `hello()` method to take a variable `name`.

```python
def hello(name):
  """Print "Hello " and a name and return None"""
  print("Hello", name)

...

hello("Josephine")

```

>After running the script, in the IPython console, type `hello("Napoleon")` or any other name

#### Challenge
Change the call function to loop over a few names (your first spamming script!).

### External Arguments
But these are still variables defined in the script, how do we pass variables in from the command line?
There is a library called `sys` which allows your script to read from the **system** in which it is running.  Variables passed in are called `arguments` and can be read from an array called `sys.argv`

In a new script called *sysargs.py*, type:

```python
import sys
# main program starts here
if __name__ == '__main__':
  program = sys.argv[0]
  print("Program running is:", program)
```

Only one argument is present and that is the name of the program which is running - this will always be the case.
We will now include two extra arguments so add some extra lines to the code:

```python
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
```
1. In Spyder, we can add the extra arguments by:
    1. **Run** -> **Configure**
    1. Check **Command line options** then enter "hello world" in the text field
    1. Click on **OK**
1. OR you can run directly from the terminal window as `python sysargs.py hello world`
1. Now run the script and you will see the arguments have been passed into your script.


#### Challenge
Return to your `hello.py` script and allow the name to be entered as an argument

```python
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

```

>**WARNING!!**  Allowing information to be passed into your script this way is VERY DANGEROUS.  The `argv` array should never be read directly without checking the validity of the contents first.

### ArgParse: Safe use of external arguments
To help you with checking that nothing malicious is passed into your script, use a library called `argparse`.
The `argparse` module makes it easy to write user-friendly command-line interfaces. The program defines what arguments it requires, and `argparse` will figure out how to parse those out of `sys.argv`. The `argparse` module also automatically generates help and usage messages and issues errors when users give the program invalid arguments.

We will update the previous script:

```python
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

```

1. As before, use the **Run** -> **Configure** to add **Command-line options** `--randomname Napoleon`, 'OK'
1. Now **Run**

-----
We will now move onto the next lesson <a class="btn btn-info" href="2-errors">Handling errors</a>
