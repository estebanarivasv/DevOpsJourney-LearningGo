'''
Operators: special characters that have special meanings that are recognized by Python.
- Math operators: +, -, *, / 
'''
print(1 + 4) # 5
print(5 - 2.6) # 2.4
print(32 * 8) # 256
print(17 / 3) # 5.666666666666667

'''
Order of Operations
Parentheses - (): used to group  different operations to manipulate the order that are performed
'''
print (6 * 3 - 10) # Subtraction is done after multiplication - result: 8
print (6 * (3 - 10)) # Multiplication is done after subtraction - result: -42

'''
Not-commonly-known Operators - These are space sensitive
Exponentiation - **: raise one number to another power.
Integer Division - //: least important. Rounds down the division.
Modulo - %: aka Remainder operator. --- If the reminder is a 0, it is an even number. Otherwise, we have an odd number.
'''
# Exponentiation - **
print (4 ** 3) # Four times four times four - result: 4 * 4 * 4 = 64

# Integer Division - //
print (10 / 3) # Normal division - result: 3.3333333333333335
print (10 // 3) # Rounds down near to zero - result: 3

print (10 / -3) # Normal division in negative numbers - result: -3.3333333333333335
print (10 // -3) # Rounds down further from zero - result: -4

# Modulo - %
print (38 % 3) # 10 goes into 38 12 times with a REMAINDER OF 2 --- result: 2