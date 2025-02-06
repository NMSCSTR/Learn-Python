"""
Perform built-in function in the list being provided
based on the different processes below

"""
#Using lists(Dynamic Arrays)
array = [10, 20, 40, 20, 30, 40, 50]
#Accessing elements(5pts)
print(array[3]) #Syntax print(list_name[index])
#Modifying elements(5pts)
array[2] = 231 # list_name[index] = newValue
#Adding elements(10pts)
array.append(45) # list_name.append(value)
array.insert(2, 455) # list_name.insert(index, value)
#Removing elements(10pts)
array.pop() # list_name.pop()
array.remove(20) # list_name.remove(element)
#checking existence(5pts)
print(20 in array) # print(element in list_name) True
#Iterating through an array(10pts)
for num in array:
    print(num, end="->")
"""
FULL NAME OF OUR 
CICT DEAN
"""
