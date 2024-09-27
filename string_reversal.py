'''
Simple (broken) program to reverse a string.  Look for 'BUG' to find the bug.

Takes in a string of arbitrary (but assumed to be non-zero) length; returns a 
string of the same length, but reversed.
'''
# I change the name of the function on purpose
def reverse_string_my(mystring):
    '''
    Reverses the ordering of characters in a string using a simple loop.
    Input: a string.
    Output: a completely reversed version of that string, including all characters.
    '''
    
    reversed_string_my= ""

    if len(mystring)  ==0 :
    
        return ""
    
    # BUG: the 0 in the range() method should be -1, given how range() works!
    for i in range(len( mystring)-1,-1,-1 ):  
        
        
        
        reversed_string_my += mystring[ i ]
    
    return reversed_string_my

mystring="Go green!"

print("\noriginal string:    ",mystring,"\n")
reversed = reverse_string_my(mystring)



print("reversed string:    ",reversed,"\n")
