'''
String operators: operators applied to strings.
- Concatenation - +: 
    - The plus sign does not add strings mathematically.
    - It smashes two strings together. 
    - It can't concatenate an int and a str together.
- Multiplication - *: 
    - You can't multiply a string by string
    - You can multiply a string by a number
'''

# 1. Concatenation
print("hello" + "world") # helloworld

first_name = "Steve"
last_name = "Brown"
full_name = first_name + last_name
print(full_name) # SteveBrown

# If we concatenate string numbers, Python treats them as any other str.
print("5" + "3") # 53


# 2. Multiplication
print("hi" * 3) # hihihi