# Arrays are super useful in programming because they allow you to store multiple values
# in one variable.
cars = ["Jeep", "Audi", "BMW"]
# Having an array of cars in easier than having:
car1 = "Jeep"
car2 = "Audi"
car3 = "BMW"

# To Access the elements of an array, you use the index number. The start of tha array is 
# index 0 and goes on from there. If you want the last element in an array, you would use 
# a -1 and then work backwards from there. 
# ['a', 'b', 'c', 'd', 'e']
#   0    1    2    3    4 
#  -5   -4   -3   -2   -1
# So you can access the first element of the cars array by doing this:

print("Example 1")
firstCar = cars[0]
print(firstCar)

print(cars[1])

# You can also use the index to modify what is stored at that index in the array. For example,
# if you wanted to change "Audi" in the cars array to "Chevy" you would do this:

print("Example 2")
print(cars[1])
cars[1] = "Chevy"
print(cars[1])

# You can use the function len() to get the length of any array 

print("Example 3")
length = len(cars)
print(length)

# You can also loop over the elements in an array

print("Example 4")
for x in cars:
    print(x)

# If you want to add an element to the end of an array, you would use the function append()

print("Example 5")
print(cars)
cars.append("GMC")

# You can use the pop function or the remove function to remove elements from an array. When using
# the pop function, you use the index number. When using the remove function, you use the element.
# If you are using the remove fuction, it only removes the first occurance of the element

print("Example 6")
print(cars)
cars.pop(2)
cars.remove("Chevy")
print(cars)

# There are a lot of different functions that you can use with arrays as well. Here is a short list
# of some functions you can do with arrays. You use them the same way that you use the functions listed
# above e.g. array.function()

# append(*) -  Adds an element to the end of a array
# clear()   -  Removes all elements from the array
# copy()    -  Returns a copy of the array
# count(*)  -  Returns the number of elements with the specified value
# extend(*) -  Add the elements of an array to the end of the current array
# index(*)  -  Returns the index of the first element with the specified value
# insert(*) -  Adds an element at the specified position
# pop(*)    -  Removes the element at the specified position
# remove(*) -  Removes the first element with the specified value
# reverse() -  Reverses the order of the list
# sort()    -  Sorts the list

print("Example 7")
print(cars, '\n')

cars.append("Ford")
print(cars, '\n')

newCars = cars.copy()
print(cars, newCars, '\n')

cars.clear()
print(cars, '\n')

Jeeps = newCars.count("Jeep")
print(Jeeps, '\n')

moreCars = ["Audi", "BMW", "Chevy"]
newCars.extend(moreCars)
print(newCars, '\n')

print(newCars.index("Audi"), '\n')

newCars.insert(2, "Tesla")
print(newCars, '\n')

newCars.pop(3)
print(newCars, '\n')

newCars.remove("Tesla")
print(newCars, '\n')

print(newCars)
newCars.reverse()
print(newCars, '\n')

newCars.sort()
print(newCars, '\n')

# You can also create an array from user input using a for loop (You'll learn more about this in the next lesson)
print("Example 8")
newArray = []
for x in range(5):
    nextInt = int(input("Enter a number: "))
    newArray.append(nextInt)
print(newArray)
