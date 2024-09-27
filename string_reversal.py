'''
Simple (broken) program to reverse a string.  Look for 'BUG' to find the bug.

Takes in a string of arbitrary (but assumed to be non-zero) length; returns a 
string of the same length, but reversed.
'''

def reverse_string(mystring):
    '''Reverses the ordering of the string
    
    Inputs: 
        - mystring: a string
        
    Output:
        - reversed_string: a reversed version of the original string
    '''
    
    reversed_string = " "

    if len(mystring) == 0:
        return []
    
    # BUG: the 0 in the range() method should be -1, given how range() works!
    for i in range(len( mystring)-1, 0, -1):  
        reversed_string += mystring[i]
    
    return reversed_string

mystring="Go green!"

print("Original string: ",mystring,"\n")
reversed = reverse_string(mystring)
print("Reversed string: ",reversed,"\n")