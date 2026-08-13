# there are different data structures in python it helps to store & organize data
# the main data structures are: lists, tuples, sets, and dictionaries

# 1. LISTS []
# Ordered, Mutable , Allows Duplicates
# %%
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
# %%
colors.append("black")  # 'append' adds element at last
print(colors)
# %%
colors.insert(1, "yellow")  # 'insert' adds element at index 1
print(colors)
# %%
colors.remove("blue")  # 'remove' finds & removes the element from first
print(colors)
colors.remove("blue")  # two remove again run the method again
print(colors)
# %%
colors.pop()  # 'pop' removes the last element
print(colors)
print(colors.pop())  # this gives back last element'
print(colors)
# %%
colors.sort()  # 'sort' arranges the elements in a order
print(colors)
# %%

# LOOPING THROUGH LIST
for another_color_list in colors:
    print(another_color_list)
# %%

# 2. TUPLE ()
# Ordered, Immutable, Allows Duplicates

numbers = (2, 6, 3, 5, 8, 4, 9)
print(numbers)

# %%
# ACCESSING ELEMENTS
# same method as LISTs

print(numbers[0])   # gives first element
print(numbers[1:3]) # gives 1st & 2nd elements
print(numbers[1:4]) # gives 1st,2nd & 3rd elements
print(numbers[0:])  # gives all elements
print(numbers[-1])  # gives the last element
print(numbers[-2])  # gives the 2nd last element
# %%
numbers[0]="brown" # causes erros bcuz tuple is immutable

# %%
# TUPLE METHODS

print(numbers.count(2))  # 'count'--> the no. of times a element is repeated
print(numbers.index(9))  # 'used'--> to know the index of a element

print("No. 2 is repeated", numbers.count(2), "time")
print("No. 4 is at the index :", numbers.index(4))

# %%
