'''
Assignment Operators: Variables + updating the value of a variable
- Change the value of the current existing value

Types:
- +=: means "take the current value of the variable, update it to 
be the current variable plus what is in the right side"
- -=: means "take the current value of the variable, update it to 
be the current variable minus what is in the right side"
- *=: Multiplication
- /=: Division
- //=: Integer division
- **=: Exponentiation
- %=: Modulus

'''
monthly_income = 3000
monthly_income = monthly_income + 50
print(monthly_income) # 3050

monthly_income += 750
print(monthly_income) # 3800

rent = 500
monthly_income -= rent
print(monthly_income) # 3300