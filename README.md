Use this module to easily parse a single, unique 
code containing as much information as your 
function or program needs, much as the bash 
'chmod' command extracts 3 different file
permissions from each number in 775. 

|     Code      |   Flags     |
|:-------------:|:----------------:|
| 1             |      [1]         |
| 2             |   [2]            |
| 3             |  [1, 2]          |
| 4             |   [3]            |
| 5             |    [1, 3]        |
| 6             |    [2, 3]        |
| 7             |    [1, 2, 3]     |
| 8             |    [4]           |
| 9             |    [1, 4]        |

... and so on. This system relies on the fact that 
any integer can be broken down into a unique set of 
the members of the sequence y = 2^n. Basically, 
these are the members of the base-2 number system
which can be represented with just a single digit set,
which is to say they are capable of hold the most 
information.

Usage
=============

Outside of a programmatic interface, call for example:

```python

PRINT = 0
MODIFY = 1
EXTRACT = 2
ANNOTATE = 3
ACCESSIBILITY = 4

some_api(doc, seq.code([PRINT, ANNOTATE, ACCESSIBILITY]))

```

... specifying an arbitrary number of desired behaviors.
Inside that inferface, call:

```python

def some_api(doc, code):
    behaviors = seq.flags(code)

    # can't modify
    if MODIFY in behaviors:
        change_stuff(doc)

    # can print
    if PRINT in behaviors:
        queue_print(doc)

```

... and retrieve the list of integers, each representing
a single behavior. Then do something with all that power!
