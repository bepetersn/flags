import math 

"""
 
"""
    

""" Returns the nth member of the 2^n sequence. """
def seq(n, base=0):
    return 2 ** (n-base)


""" Retrieves the flag, or index, of the highest member of the
    2^n sequence contained within a code. """
def highest_flag(code, base=0):
    return int(math.log(code, 2)) + base


""" Returns the flags that make up your code. """
def flags(code, base=0):
    import pdb; pdb.set_trace()
    if code > 0:
        highest = highest_flag(code, base)
        return flags(code-seq(highest, base), base) + [highest]
    return []

""" Returns the members of the 2^n sequence that sum to your code. """
def parts(code, base=0):
    return [seq(f, base) for f in flags(code, base)]


""" Returns the code corresponding to a certain list of flags. """
def code(flags, base=0):
    return sum([seq(f, base) for f in flags])
    