# WHILE LOOP --> repeats the code as long as the condition is true

i = 2  # start from 2
while i <= 10:  # checks the condition everytime until its false
    print(i)
    i += 1
# without increament the loop will be infinite

# in for loop range() controls the increaments & start, stop, step
# in while loop we have to do it on our own

# WHILE LOOP WITH CONDITIONAL STMTS :

count = 1  # start at 2
while count <= 14:
    if count % 2 == 0:
        print(count, "is even")
    else:
        print(count, "is odd")
    count += 1

# WHILE LOOP WITH CONTINUE/BREAK STMTS :

count = 0
while count < 10:
    
    if count % 2 == 0:
        continue  # skips even nmbrs
    print(count)
    count += 1

count = 1
while count < 11:
    if count == 8:
        break  # break at 8
    print(count)
    count += 1

# NESTED LOOPS --> means a loop inside another loop

# when outer loop runs once, inner loops runs completely
for a in range(2):
    print("outer loop")
    for z in range(3):
        print("inner loop")

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
