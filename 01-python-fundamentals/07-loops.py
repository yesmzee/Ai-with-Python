# LOOPS --> loops repeat a block of code mutliple times

# in python there are only two types :
# for loop & while loop

# for loop

for i in range(5):  # prints numbers 0 1 2 3 4
    print(i)

for i in range(6):  # prints the message 6 times
    print("zeeshan is learning python")
    print("python is boring compared to cpp")

# another way to use for loop

for z in range(4):
    print("this is line", z)

# character by character printing :

for m in "zeeshan":  # prints char by char
    print(m)

for m in "zeeshan", "ali":  # works same as tuple ("zeeshan", "ali")
    print(m)

# for loop with lists

for name in ["zeeshan", "ali", "ahmed"]:
    print(name)


# 4x4 matrix just from the course : its kind of advanced but learned the concept by ai

i = 4
rows = 4
cols = 4
matrix = []
for r in range(rows):
    row = []
    for c in range(cols):
        row.append(0)  # --> adds 0 everytime and final row = [0,0,0,0]
    matrix.append(
        row
    )  # --> final matrix = [ [0,0,0,0] , [0,0,0,0] , [0,0,0,0] , [0,0,0,0] ]
for row in matrix:
    print(" ".join(map(str, row)))  # --> my pov this removes [] + , and:

# provides clean output of 4x4 matrix like :

#   0 0 0 0           without it : [ [0,0,0,0],
#   0 0 0 0                          [0,0,0,0],
#   0 0 0 0                          [0,0,0,0],
#   0 0 0 0                          [0,0,0,0] ]

# -------------------------------------------------------------------------


# star pyramind using for loop

rows = 10  # more the rows more bigger the pyramid

for level in range(1, rows + 1):  # -----> this is for from where start & stop the loop
    print(" " * (rows - level) + "*" * (2 * level - 1))

# in python character, string literal ' ' , strings can be multiplied with a integer number (only)

# so the code prints the spaces and stars one by one which gives a star pyramid
