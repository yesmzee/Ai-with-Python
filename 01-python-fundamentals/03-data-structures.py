#DATA STRUCTURES :
# there are different data structures in python it helps to store & organize data
# the main data structures are:
# LISTS
# TUPLES
# SETS
# DICTIONARIES
#--------------------------------------------------------------------------------


# 1. LISTS []
# Ordered, Mutable , Allows Duplicates

colors = [ "red","blue","green","orange","blue","white",]
print(colors)

# ACCESSING ELEMENTS

print(colors[0])   # gives first element
print(colors[1:3]) # gives 1st & 2nd elements
print(colors[1:4]) # gives 1st,2nd & 3rd elements
print(colors[0:])  # gives all elements
print(colors[-1])  # gives the last element
print(colors[-2])  # gives the 2nd last element

# LIST METHODS

colors.append("black")  # 'append' adds element at last
print(colors)

colors.insert(1, "yellow")  # 'insert' adds element at index 1
print(colors)

colors.remove("blue")  # 'remove' finds & removes the element from first
print(colors)
colors.remove("blue")  # two remove again run the method again
print(colors)

colors.pop()  # 'pop' removes the last element
print(colors)
print(colors.pop())  # this gives back last element
print(colors)

colors.sort()  # 'sort' arranges the elements in a order
print(colors)


# LOOPING THROUGH LIST
for another_color_list in colors:
    print(another_color_list)


# 2. TUPLE ()
# Ordered, Immutable, Allows Duplicates

numbers = (2, 6, 3, 5, 8, 4, 9)
print(numbers)

# ACCESSING ELEMENTS
# same method as LISTs

print(numbers[0])   # gives first element
print(numbers[1:3]) # gives 1st & 2nd elements
print(numbers[1:4]) # gives 1st,2nd & 3rd elements
print(numbers[0:])  # gives all elements
print(numbers[-1])  # gives the last element
print(numbers[-2])  # gives the 2nd last element

numbers[0]="brown" # causes erros bcuz tuple is immutable

# TUPLE METHODS

print(numbers.count(2))  # 'count'--> the no. of times a element is repeated
print(numbers.index(9))  # 'used'--> to know the index of a element

print("No. 2 is repeated", numbers.count(2), "time")
print("No. 4 is at the index :", numbers.index(4))


# 3. SETS {}
# Unorderd , Mutable , No-duplicates

zee_set = {1, 2, 3, 4, 5, 5, 6} # will not have duplicates
print(zee_set)

#  SET METHODS
zee_set.add(9)  # 'add' adds 9 to the set
print(zee_set)

zee_set.remove(4)  # 'remove' removes 4 from set
print(zee_set)

# SETS OPERATIONS

A = {1, 2, 3, 4}
B = {4, 5, 6}

print(A.union(B))  # combines all element & no duplicates
print(A.intersection(B))  # only common elements
print(A.difference(B))  # only elements from set-A (1st-set) not in set-B (2nd-set)


# 4.DICTIONARY {}
# Unordered, Mutable, Key-value pairs

student = {"name": "Zeeshan", "age": 22, "dept.": "AI"}
print(student)

# ACCESSING VALUES

print(student["name"])
print(student.get("age"))

# DICTIONARY METHODS

student["age"]=23 # this updates to new value 23
print(student)

student["city"]="Gigit" # this adds new key & value
print(student)

student.pop("dept.") # this removes dept.
print(student)


# LOOPING DICTIONARY

for key, value in student.items():
    print(key,"=", value)

