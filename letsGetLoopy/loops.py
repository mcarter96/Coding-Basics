# Sometimes when writing a program, you want to go through a number of lines multiple times.
# This is where it's helpful to have loops. They are used for iterating over a sequence.

# For Loops
# You can use for loops in python in a couple different ways. The first way you can use them
# is to iterate over a list/array
print("Example 1")
pets = ["dog", "cat", "bird", "snake", "rabbit"]
for x in pets:
    print(x)

# On the first pass through, the first object from the list is read into x,
# then because the statement in the loop is to print(x), it prints out "dog".
# Then it continues going through the loop until it reaches the end of the list

# Since strings are arrays of chars, you can iterate through each letter in a string
print("Example 2")
word = "computer"
for x in word:
    print(x)

print("and")

for x in "monitor":
    print(x)

# If you want to stop the loop at any point before it is finished running, you can 
# use the keyword "break". This will exit the loops and execute the commands
# following the loops

print("Example 3")
cars = ["Yukon", "Jeep", "BMW", "Audi", "Equinox"]
for x in cars:
    print(x)
    if x == "BMW":
        break
print("The next step")

for x in cars:
    if x == "Audi":
        break
    print(x)
print("After the loop")

# You can use the keyword "continue" to stop the current iteratino and move onto the next one

print("Example 4")
instruments = ["trumpet", "saxophone", "drums", "clairnet", "trombone"]
for x in instruments:
    if x == "drums":
        continue
    print(x)
print("End of the list")

# You can also use a for loop to iterate over a specific number of times. You
# do this by using the range() function 

print("Example 5")
for x in range(6):
    print(x)

# Notice that it still starts at 0 and goes to just one number below the range.
# If you wanted to print out the first 6 numbers not including 0, you would just
# do this

print("Example 6")
for x in range(6):
    print(x+1)

# If you want the number range to not start at 0, you can use two numbers as your
# parameters for the range function. It will start at the first parameter and go up to 
# the second parameter, but not include the second parameter

print("Example 7")
for x in range(5, 10):
    print(x)

# You can also increment by numbers other than 1 if you want. Say if you wanted to print
# all the numbers from 0 to 100 that are multiples of 10. You would add a third parameter
# for how much you want to increment by each time.

print("Example 8")
for x in range(0, 101, 10):
    print(x)

# Note: I go to 101 because I want 100 to be printed as well, so the 101 makes sure to include it

# You can have nested for loops. Which means inside of a for loop, the command that is executed is another for loop.
# For each iteration of the outer loop, the inner loop will run through all of it's iterations

print("Example 9")
for x in range(5):
    for y in range(5):
        print("*", end=' ')
    print("*")

# Note: the parameter "end=''" allows you to change what is printed after the print statement. The default is 
# newline. In the example, I have it put a space after it prints each object, but you can have it be anything
# that you want it to be.