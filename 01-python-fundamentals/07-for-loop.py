# LOOPS --> loops repeat a block of code mutliple times

# in python there are only two types :
# for loop & while loop

# FOR LOOP --> used when we how many times something should repeat

for i in range(5):  # stop at 5 (5 not included)
    print(i)  # prints 0 1 2 3 4

# in python range() is used to generate a sequence of numbers, which is used to control the loop.

for i in range(1, 5):  # start at 1 & stop at 5
    print(i)  # prints 1 2 3 4

# in python range() can take 3 arguments : start, stop, step

for i in range(2, 15, 2):  # start at 2 , stop at 15 , move steps by 2
    print(i)  # prints 2 4 6 8 10 12 14

# ANOTHER WAY TO USE FOR LOOP :

for z in range(4):
    print("this is line", z)

# CHARACTER BY CHARACTER PRINTING :

for m in "zeeshan":  # prints char by char
    print(m)

for m in "zeeshan", "ali":  # works same as tuple ("zeeshan", "ali")
    print(m) # zeeshan ali

# FOR LOOP WITH LISTS

student = ["zeeshan", "ali", "ahmed"]
for name in student:
    print(name) # zeeshan ali ahmed

# FOR LOOP WITH CONDITIONAL STMTS :

for i in range(2,12,2):
    if i == 9:
        print("founded 9 !")
    else:
        print(i)

for z in range(1,15):
    if z%2==0:
        print( z, "is even")
    else:
        print(z, "is odd")

#  FOR LOOP WITH CONTINUE/BREAK STMTS :

for i in range(1,10):
    if i ==2:
        continue # continue here skips 2 
    print(i) # 1 3 4 5 6 7 8 9

for m in range(1,8):
    if m == 6:
        break # break stops the loop before 6
    print(m) # 1 2 3 4 5

#   FOR LOOP WITH CONDITIONALS + BREAK/CONTINUE STMTS :

for f in range(1,12):
    if f == 10:
        break
    if f % 2 == 0: 
        continue # skips even numbers
    print(f)

# 4X4 MATRIX just from the course : its kind of advanced but learned the concept

i = 4
rows = 4
cols = 4
matrix = []
for r in range(rows):
    row = []
    for c in range(cols):
        row.append(0)  # --> adds 0 everytime and final row = [0,0,0,0]
    matrix.append(row)  # --> final matrix = [ [0,0,0,0] , [0,0,0,0] , [0,0,0,0] , [0,0,0,0] ]
for row in matrix:
    print(" ".join(map(str, row)))  # --> my pov this removes [] , and:
# provides clean output of 4x4 matrix like :

#   0 0 0 0           without it : [ [0,0,0,0],
#   0 0 0 0                          [0,0,0,0],
#   0 0 0 0                          [0,0,0,0],
#   0 0 0 0                          [0,0,0,0] ]

# -------------------------------------------------------------------------

# STAR PYRAMIND USING FOR LOOP :

rows = 10  # more the rows more bigger the pyramid

for level in range(1, rows + 1):  # -----> this is for from where start & stop the loop
    print(" " * (rows - level) + "*" * (2 * level - 1))

# in python character, string literal ' ' , strings can be multiplied with a integer number (only)

# so the code prints the spaces and stars one by one which gives a star pyramid

# ----------------------------------THE END----------------------------------