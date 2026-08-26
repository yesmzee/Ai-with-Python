# NESTED LOOPS --> means a loop inside another loop

# when outer loop runs once, inner loops runs completely

for a in range(2):
    print("outer loop")

    for z in range(3):
        print("inner loop")

# 4 x 4 MATRIX :

i = 4
rows = 4
cols = 4
matrix = []

for r in range(rows):
    row = []

    for c in range(cols):
        row.append(0)
    matrix.append(row)

for row in matrix:
    print(" ".join(map(str, row)))

# NUMBER PATTERN :

for i in range(3):
    for j in range(3):
        print(i, j) 

# TABLE PATTERN :

for i in range(2, 6):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)

# INCREASING STARS :

for row in range(1, 5):
    for column in range(row):
        print("*", end=" ")
    print()

# DECREASING STARS :

for row in range(4, 0, -1):
    for column in range(row):
        print("*", end=" ")
    print()

# NUMBERS PYRAMID :

rows = 5
for i in range(1, rows + 1):

    for j in range(i):
        print(i, end=" ")
    print()  
