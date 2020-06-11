# Part 1
# Use functions to get the sum from a series (you decide the number) of numbers that the user inputs
# Part 2
# Use functions to get the max number from the series of numbers already inputed by the user
# 
# Example Output:
# Enter the first number: 4
# Enter the second number: 1
# Enter the third number: 5
# Enter the fourth number: 6
# The sum of your numbers is: 16
# The max number is: 6

#Part 1

def addition(x,y):
    return x + y

def add():
    numberOne = int(input("Enter 1st Value:  "))
    numberTwo = int(input("Enter 2nd Value:  ")) 
    sumTotal = addition(numberOne,numberTwo)
    return sumTotal


#Part 2


def coolerAddition(a,b,c,d):
    return a+b+c+d

def findSum():
    valueOne= int(input("Enter 1st Number:  "))
    valueTwo= int(input("Enter 2nd Number:  "))
    valueThree= int(input("Enter 3rd Number:  "))
    valueFour= int(input("Enter 4th Number:  "))
    anwser = coolerAddition(valueOne, valueTwo, valueThree, valueFour)
    return anwser

def question():
    print ("Addition(1) or cooler Addition(2)")
    questionanwser= int(input())
    if questionanwser == 1:
        print(add())
    elif questionanwser == 2:
        print(findSum())

print(question())
