# Getting input from the keyboard

stringInput = input("Enter a name: ")
print(type(stringInput), stringInput)

# You can now use the input from the computer just like any other variable that you have

# Type Casting: turning one type of data type into another
# Useful for when you have input from the computer that you want to be in numerical form

x = '65'
print(type(x), x)
x = int(x)
print(type(x), x+5)

# Use casting when getting input from the user to make sure that they enter the correct form of data

intInput = int(input("Enter a number: "))
print(type(intInput), intInput)

floatInput = float(input("Enter a decimal number: "))
print(type(floatInput), floatInput)

print(type(x), x)