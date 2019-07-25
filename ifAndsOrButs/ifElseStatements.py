# There are a couple different ways to handle logic in your programs. There are booleans which are either True or False
# You can use these booleans to determine if your code should go down a specific branch or not.

# An important note before we start going into the logic is comparing two values. When you set a variable, you use a single
# "=". If you were to use this in the statement [if x = 5], then you would have just set the variable x to 5. So we use a 
# "==" to signify that we are comparing the two variables. You can use >, >=, <, <= as well 

# The first way to handle logic is and if-else statement. They look like this

exampleBoolean = True
if exampleBoolean == True:
    print("Hello world")
else:
    print("The world does not say hello")

# Notice how the print statement in the else section does not get printed. That is because the first statement is true,
# so it runs that block of code until the end then skips out of the entire if-else statement. If we were to change the
# value of the boolean to be False (or any other value), then you would get just the else statement.

exampleBoolean = 5
if exampleBoolean == True:
    print("Hello world")
else:
    print("The world does not say hello")

# You can also use if statements with certain values to check ints, floats, strings, etc. 

age = 16
if age <= 16:
    print("You cannont drive")
else:
    print("You can drive")

# If you had an if-else statement with multiple if statements, what do you think would happen?

age = 21
# Statement 1
if age < 21:
    print("You can't drink")
# Statement 2
if age == 21:
    print("Happy birthday! You can drink")
# Statement 3
if age > 21:
    print("Of course you can drink")
else:
    print("That's not a real age")

# Notice how the else statement still prints? That's because the computer is going through each individual if statement
# and looking for an else statement. So when it gets to the last if statement, it sees the else statement and prints that.
# There is an elif statement which will run after the first if statement. This way, you can have multiple if statements
# attached to one else statement

weather = 75
if weather < 60:
    print("It's cold, better bring a jacket")
elif weather < 90:
    print("It's gonna be warm, but not too hot")
elif weather > 91:
    print("Holy crap it's gonna be hot")
else:
    print("I'm not too sure about this weather")

# Notice how this only prints out the one statement that the if statement is true for and doesn't test any of the rest.
# There is a syntax problem with this problem. To avoid any future errors from any possible overlap, we would want to
# add in a lowerbound value for each one too. To do this, we will use the keyword "and" which means as long as the variable
# matches both of the constraints, the if statement will run

weather = 85
if weather < 60:
    print("It's cold, better bring a jacket")
elif weather >= 60 and weather < 90:
    print("It's gonna be warm, but not too hot")
elif weather >= 90:
    print("Holy crap it's gonna be hot")
else:
    print("I'm not too sure about this weather")

# We can also use the keyword "or" to mean if either of the constraints in the if statement are met, then that statement will run.

goToMovie = True
goToPark = False
if goToMovie == True or goToPark == False:
    print("Get in the car")
else:
    print("Find something else to do")