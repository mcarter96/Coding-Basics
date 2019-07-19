# Write a program that asks the user for their name and respond "Hello, [their name]"
# Come up with three different questions to ask the user and print them out in a list under their name 
stringInput = input("Insert Full Name:")
print (type(stringInput),"Hello,", stringInput, ".  Set up your profile by anwsering some basic questions.")
# Your variable names shouldn't be "stringinput" and "Stringinput". That's too confusing and can hurt you down the line
# You should come up with variable names that tell you what they are. Also, it's standard practice to use camel case,
# which means that the first word is lowercase, then any following words are capitalized e.g. thisIsMyVariableName 
stringinput = input("What is your gender?  ")
intinput = int(input("How old are you?  ")) 
Stringinput = input("What city/ town do you live in?  ")
print()
print()
print("Profile:")
# You don't need to print the type with each statment. That was just to show you what data type was being used
# You can just use print("Name: ", stringInput)
print(type(stringInput), "Name:",stringInput)
print (type(stringinput), "Gender:",stringinput)
print(type(intinput), "Age:",intinput)
print(type(Stringinput),"From:", Stringinput)
print(type(stringInput),"Welcome", stringInput, ",  You have up finshed signing up for Virus.com")
# That's pretty funny

# In general, you shold work on standard coding syntax.
# Lines should be seperated by the function they do and there should be spaces after commas
# Make it look nice and pretty so that someone else can come in and look at it easily
# I copied what you wrote and cleaned it up a little bit below

# Part 1
nameInput = input("Insert Full Name: ")
print("Hello, ", nameInput, ". Set up your profile by anwsering some basic questions.")

# Part 2
genderInput = input("What is your gender? ")
ageInput = int(input("How old are you? ")) 
fromInput = input("What city/ town do you live in? ")

print()
print()

print("Profile:")
print("Name:", nameInput)
print ("Gender:", genderInput)
print("Age:", ageInput)
print("From:", fromInput)
print("Welcome", nameInput, ", you have up finshed signing up for Virus.com")