import math 

"""
 
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
    
    
