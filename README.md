ses
------

Use this module to easily parse a single, unique 
code containing as much information as your 
function or program needs, in the same way that the 
bash `chmod` command extracts 3 different file
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

|     Code      |   Gives You      |
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
any number can be broken down into a unique set of 
the members of the sequence y = x^(n-1). That's what 
I've eruditely called the Sub-Exponential Sequence, 
or SES, for short.

If instead of the indices, you want to get back the
actual component parts of your code, use ses.parts().
Finally, if you want to find out what code you need to 
get back a certain list of indices, pass your list into
ses.code(). 

--------------------------

Simple example:

    import ses
    
    # takes a list of tokens, and a code 
    # denoting which ngrams to look at.
    def handle_ngrams(tokens, code):
        n_grams = ses.indices(code)
        if 1 in n_grams:
            # do something with the unigrams
        if 2 in n_grams:
            # something with bigrams
        if 3 in n_grams:
            # something with trigrams
        if 4 in n_grams:
            # something with quadrigrams
    
    tokens = ['No', 'star', 'is', 'o\'er', 'the', 'lake', ',' 'its' 'pale', 'watch', 'keeping']
    
    # looks at the sentence's two- and three-word combinations, but nothing else.
    handle_ngrams(tokens, ses.code([2, 3]))
    
As you can see, `ses` makes passing information to your functions simple, and conceivably makes abstraction even simpler.

