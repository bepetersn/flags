""" Use this module to easily parse a single, unique 
    code containing as much information as your 
    function or program needs, much as the bash 
    'chmod' command extracts 3 different file
    permissions from each number in 777. In fact, this 
    module is based on that system, but has been 
    greatly extended.  

    If your algorithm can do any combination of 2, 3, 4, 
    or any number of related things, but you want only 
    one code to specify that behavior, this is all 
    you need. 

    Get the ses module on your system. Import it. 
    Then pass into ses.indices() any code that denotes
    some specific set of functionality--which is any
    whole number at all. What you get back is a list
    of integers.

    Here's how it works: 
     code | gives you
    ++++++|++++++++++++++++
       1  |  [1] 
       2  |  [2]
       3  |  [1, 2]
       4  |  [3]
       5  |  [1, 3]
       6  |  [2, 3]
       7  |  [1, 2, 3]
       8  |  [4]
       9  |  [1, 4]

    ... and so on. This system relies on the fact that 
    any number can be broken down into a unique set of 
    the members of the sequence y = x^(n-1). That's what 
    I've eruditely called the Sub-Exponential Sequence, 
    or SES, for short.

    If instead of the indices, you want to get back the
    actual component parts of your code, use ses.parts().
    Finally, if you want to find out what code you need to 
    get back a certain list of indices, pass your list into
    ses.code(). """
    

""" Returns the nth member of the SES. """
def ses(n):
    return 2 ** (n-1) 


""" Retrieves the index of the highest member of the SES
    contained within a code. """
def find_highest_index(code):
    for i in range(1, code+1):
        member = ses(i+1)
        if code < member:
            return i


""" Returns the indices of the SES members that make up your code. """
def indices(code):
    indices = []
    while code > 0:
        highest_index = find_highest_index(code)
        indices.append(highest_index)
        code -= ses(highest_index)
    indices.sort()
    return indices


""" Returns the components of the SES that sum to your code. """
def parts(code):
    return [ses(index) for index in indices(code)]


""" Returns the code corresponding to a certain list of numbers. """
def code(indices):
    return sum(ses(index) for index in indices)
    
    
