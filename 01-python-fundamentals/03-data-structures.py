# there are different data structures in python it helps to store & organize data
# the main data structures are: lists, tuples, sets, and dictionaries

# LISTS
# Ordered, Mutable , Allows Duplicates
#%%
colors = [ "red","blue","green","orange","blue","white",]
print(colors)

# ACCESSING ELEMENTS 

print(colors[0]) # gives first element
print(colors[1:3]) #gives 1st & 2nd elements
print(colors[1:4]) #gives 1st,2nd & 3rd elements
print(colors[0:]) #gives all elements
print(colors[-1]) #gives the last element
print(colors[-2]) #gives the 2nd last element

# LIST METHODS
#%%
colors.append("black") # 'append' adds element at last
print(colors)
# %%
colors.insert(1,"yellow") # 'insert' adds element at index 1
print(colors)
# %%
colors.remove("blue") # 'remove' finds & removes the element from first
print(colors)
colors.remove("blue") # two remove again run the method again
print(colors)
# %%
colors.pop() # 'pop' removes the last element
print(colors)
print(colors.pop()) # this gives back last element'
print(colors)
# %%
colors.sort() # 'sort' arranges the elements in a order
print(colors)
# %%

#LOOPING THROUGH LIST
for another_color_list in colors:
    print(another_color_list)
# %%
