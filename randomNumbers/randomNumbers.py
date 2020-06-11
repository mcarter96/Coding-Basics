# Sometimes you'll want to get a random number from the computer to use.
# The first thing you'll need to do is import the random package. This is
# a library of code, it's a program that somebody else wrote to accomplish
# a task so that you can just write one line of code instead of trying to 
# rewrite the complicated logic it takes to solve certain problems. You can use
# one of these packages/libraries by using the word import at the top of your program
import random

# Now that we have imported the random library, we can use it to generate random numbers
# for our program. 

print("Example 1")
randInt = random.randint(0, 100)
print(randInt)

# Now any time you run this line of code, you'll get a new random number in the range 0, 100.
# We can use for loops to generate a bunch of different random numbers. 

print("Example 2")
randInt = random.randint(0, 100)
for x in range(10):
    print(randInt)

# Notice how this prints the random number we got over and over again. That's because we called
# the random number, then just printed that number over again. If we want 10 different random 
# numbers, we have to put the random call in the loop.

print("Example 3")
for x in range(10):
    print(random.randint(0,100))

# Let's say that you want a set of random numbers that are multiples of 5. You could use this logic

print("Example 4")
for x in range(10):
    randInt = random.randint(1, 21) * 5
    print(randInt)

# Remember that the two parameters are inclusive of the first number and exclusive of the second number
