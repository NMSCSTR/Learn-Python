#Using lists(Dynamic Arrays)
array = [10, 20, 30, 40, 50]
print(array)

#Accessing elements
print(array[0])

# Modifying elements
array[1] = 25
print(array)

# Adding elements
array.append(60) #add at the end 
array.insert(2, 15) # Inserts at index 2
print(array)

#Removing elements
array.pop() # remove the last element
array.remove(15) # Remove first occurence of 15
print(array)

#checking existence
print(30 in array)

#Iterating through an array
for num in array:
    print(num, end=" ")
