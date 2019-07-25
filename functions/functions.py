# When you start making more advanced programs, you may want to repeat sections of your code over again.
# Rewriting the code is tedious and makes your code cluttered. So it is helpful to split your program up 
# into functions.

# A function is a set of statements that takes an input, computes a set of commands, and produces an output.
# You don't always need to have an input value or an output value. You define a function like so:

# def func(input):
#     # code

# The parameters are what the function will take as an input. The function will use the names of the parameters inside
# the function. When you write the function call, you write the name of the function, then a "()". If there are parameters,
# then you put them in the order that the parameters ask for. 

# def func(string, int, float)
#     newInt = int + 5 
#     newString = string[:3]
#     newFloat = float / 2.0

# func("Hello", 7, 5.0)

# Python uses indentation to determine where the function ends. So if you were to use an if-else statement or
# a loop in a function, those would need to be on their own indentation.

# def func():
#     if True:
#         if x == 5:
#            code
#     else:
#         code

# You should always have a "main" function. This will be the driver of your program so that you can keep your
# function calls all together in a clean looking way. You use the keyword "return" to return something from the 
# function. Once the computer hits the keyword "return", it will exit the function and pass the value that is
# being returned, even if there is code after it. If you don't use "return", then the function will run until it 
# reaches the end of the function


# Here is a quick example of how you would use functions

# You can return the values added together without storing them for a faster approach
def addNumbers(x, y):
    return x + y

# Or you can assign the values to a variable and then return the variable
def getNumbers():
    firstInt = int(input("Enter your first number: "))
    secondInt = int(input("Enter your second number: "))
    total = addNumbers(firstInt, secondInt)
    return total

def main():
    print(getNumbers())

# Make sure you write the function that you want to call outside of the function so that the computer knows which 
# function to call
main()


