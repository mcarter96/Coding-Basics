# Part 1
# Write a program that takes user input on what score they got on an assignment. Then use if-else statements to tell the user
# what grade they got on their assignment.
# Part 2
# Take three numbers from the user and then print them out in sequential order (from least to greatest)

#Part 1
grade= int(input("Insert grade precentage   "))

if grade >100:
    print("Stop lying")
elif grade >= 97:
    print("Good Job, A+")  
elif grade >= 93 and grade < 97:
    print("Good Job, A")
elif grade >= 90 and grade < 93:
    print("Good job, A-")
elif grade >= 87 and grade < 90:
    print ("Nice Job, B+") 
elif grade >= 83 and grade < 87:
    print("Nice Job, B")
elif grade >= 80 and grade < 83:
    print("Nice job, B-")
elif grade >= 77 and grade < 80:
    print("Try a little better next time, C+")
elif grade >= 73 and grade < 77:
    print("Try better next time, C") 
elif grade >= 70 and grade < 73:
    print("Do better next time, C-")
elif grade >= 67 and grade < 70:
    print("You need to try more, D+")
elif grade >= 63 and grade < 67:
    print("Are you even trying? D") 
elif grade >= 60 and grade < 63:
    print("You know your failing right? D-")
elif grade >= 0 and grade < 60:
    print("https://www.mcdonalds.com/us/en-us/careers.html")  

#Part 2

inputOne = int(input("Enter Number:  "))
inputTwo = int(input("Enter 2nd Number:  "))
inputThree = int(input("Enter 3rd Number:  "))

if inputOne >inputTwo and inputOne >inputThree:
    print(inputOne)
elif inputTwo > inputOne and inputTwo > inputThree:
    print(inputTwo)
elif inputThree > inputOne and inputThree > inputTwo:
    print(inputThree)

if inputTwo < inputOne and inputTwo >inputThree:
    print(inputTwo)
elif inputOne < inputTwo and inputOne > inputThree:
    print(inputOne)
elif inputThree <inputTwo and inputThree >inputOne:
    print(inputThree)

if inputOne < inputTwo and inputOne < inputThree:
    print(inputOne)
elif inputTwo < inputOne and inputTwo < inputThree:
    print(inputTwo)
elif inputThree < inputOne and inputThree <inputTwo:
    print(inputThree)