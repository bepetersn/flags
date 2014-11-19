import math 

""" Use this module to easily parse a single, unique 
    code containing as much information as your 
    function or program needs, much as the bash 
    'chmod' command extracts 3 different file
    permissions from each number in 775. 

    Here's how it works: 
     code | flags
    ++++++|++++++++++++++++
       1  |  [0] 
       2  |  [1]
       3  |  [0, 1]
       4  |  [2]
       5  |  [0, 2]
       6  |  [1, 2]
       7  |  [0, 1, 2]
       8  |  [3]
       9  |  [0, 3]

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

    some_api(doc, seq.code([0, 3, 4]))

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

    """
    

""" Returns the nth member of the 2^n sequence. """
def seq(n):
    return 2 ** n


""" Retrieves the flag, or index, of the highest member of the
    2^n sequence contained within a code. """
def highest_flag(code):
    return int(math.log(code, 2))


""" Returns the flags that make up your code. """
def flags(code):
    if code > 0:
        highest = highest_flag(code)
        return flags(code-seq(highest)) + [highest]
    return []

""" Returns the members of the 2^n sequence that sum to your code. """
def parts(code):
    return [seq(f) for f in flags(code)]


""" Returns the code corresponding to a certain list of flags. """
def code(flags):
    return sum(seq(f) for f in flags)
    
    
