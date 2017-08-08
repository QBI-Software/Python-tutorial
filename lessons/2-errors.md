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
- "A script is run from top to bottom, with import statements at the top then methods, then instructions"
- "The `sys` library connects a Python program to the system it is running on."
- "The list `sys.argv` contains the command-line arguments that a program was run with."
- "The `arparse` library is the safest way to use command line arguments"
---
# Handling Errors in Python
So we have scripts which run just fine as long as the information we give them is what they expect.  Errors appear when the script/program encounters conditions it does not know how to handle.  This is not as scary as it sounds and it is very nice to have scripts which you can feel confident are not going to "crash" as soon as someone else tries to use them.

## What can go wrong?
There are some things that will not prevent us from running a script but there are others which will.

### "Continue anyway" errors

### "Stop running if this occurs" errors
