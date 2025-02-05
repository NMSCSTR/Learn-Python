#Using lists(Dynamic Arrays)
array = [10, 20, 30, 40, 50]

#Removing elements
array.pop() # remove the last element
array.remove(40) # Remove first occurence of 15
print(array)

#checking existence
print(302 in array)

#Iterating through an array
for num in array:
    print(num, end=" ")
