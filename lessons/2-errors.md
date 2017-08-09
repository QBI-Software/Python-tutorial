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
1. Files referenced by the script need to indicate exactly where the file is so either providing the full file path or a relative file path ensures this error is avoided.
1. Files on Unix systems may have permissions set to restrict other users from viewing them.  On Windows, trying to access a file which is already open in Excel, for example, will also block the script from access.
1. A list created dynamically may not get created at all, so checking for empty lists before trying to access them is a common technique.  If items in the list are expected at a certain index (location), then the existence of that item should be tested before trying to access it.
1. Values passed in as arguments may not be what was expected by the script, so checking their type and length is a good start here.  More complex checks can also be done with pattern matching which is highly recommended.

## Syntax errors
As you create your script, it is very common to have *syntax* errors, that is, typos, incorrectly named methods or passing in the wrong number of arguments to a method.  Catching these early is easier with an editor like **Spyder**.
1. Run the following code and see the error - also note how Spyder highlights the problem.

```python
if (1 == 1)
    print("This is a syntax error")
```
You should see an output showing that something is missing:
~~~
if (1 == 1)
               ^
SyntaxError: invalid syntax
~~~


## Catching errors
Fortunately, we can catch these errors and then do something about them before they abruptly end our program.
The structure is a "try-catch-finally" block of code which is wrapped around your code.

```python
try:
  prnt("This is a name error")  #misspelt print so no method found
except NameError as e:
  print("Caught this error:", e)
finally:
  print("I'm always going to end here")

```

>The `finally` section is optional

### "Continue anyway" errors
When the error is minor, such as the first line in a text file is blank and you just want to skip it, type `continue` in the `except` block to tell the program to go to the next instruction.

### "Stop running if this occurs" errors
When the error is major and you cannot continue without the information:
1. use `break` and the program will end cleanly via the `finally` block if it is present, OR
1. use `pass` and the program will pass to the next instruction
1. only use `exit(0)` if you really want to terminate everything (in Spyder, this also shuts down the python kernel)

So, we will see how to put this in a script which reads the gapminder data as we have done in previous lessons.
