"""
Perform built-in function in the list being provided
based on the different processes below

"""
#Using lists(Dynamic Arrays)
array = ["John", "Max", "Jerry", "Jack"]
"""Accessing elements(5pts)"""
# Syntax: print(list[index])
print(array[2])
"""Modifying elements(5pts)"""
# Syntax: list[index] = new_value
array[2] = 2222
"""Adding elements(10pts)"""
# Syntax: list.append(value)
array.append(500)
# Syntax: list.insert(index, value)
array.insert(3, 111)
"""Removing elements(10pts)"""
# Syntax: list.pop()
array.pop()
# Syntax: list.remove(value)
array.remove(40)
"""checking existence(5pts)"""
# Syntax: print(elements in list)
print(20 in array) # True or false
"""Iterating through an array(10pts)"""
for num in array:
    print(num, end="\n")
for num in array:
    print(num, end=" -> ")
