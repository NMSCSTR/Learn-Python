#Using lists(Dynamic Arrays)
array = [10, 40, 20, 30, 40, 50]
#Accessing elements
print(array[2]) # specific elements to access or to be printed

# Modifying elements
array[2] = 14 # Specific elements to be modified using index

# Adding elements
array.append(60) # Insert value to the last elements
array.insert(2, 2025) # Has 2 parameter to pass which 1st: index 2nd: Value

#Removing elements
array.pop() # The last element of our list will be removed
array.remove(40) #Ang kina unhan ra nga elements ang ma remove if list have the same value

#checking existence
print(50 in array) # True or false - Type(Boolean)

#Iterating through an array
print(array)

for num in array:
    print(num, end="\n") #New line

