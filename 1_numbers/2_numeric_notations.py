'''
Numerical Notations:
# In case we want to represent 31 billion
# The following code will not represent an int, it will return a tuple instead.
'''
print(31,000,000,000)
print(type((31,000,000,000))) # tuple

'''
# We can try to define 31 billion
'''
print(31000000000)
print(type((31000000000))) # int

'''
# Or we can use the notation with the underscore to separate groups
    - Purely for human sake. Helps a lot understanding the code in the future
'''
print(31_000_000_000)
print(type((31_000_000_000))) # int


'''
Integers cannot start with a zero
'''
print(9)
#print(09) # SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers

'''
We can have leading zeroes in a float
'''
print(0.8)
print(.8)


'''
Scientific notation: sometimes Python decides to better display the numbers using scientific notations. 
'''
print(128600000000000000.0000000000000000000000000) # 1.286e+17
print(12e-10) # 1.2e-09
print(6.7e-3) # 0.0067
