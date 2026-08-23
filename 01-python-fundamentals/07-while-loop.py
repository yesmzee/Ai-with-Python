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
    count += 1
    if count % 2 == 0:
        continue  # skips even nmbrs
    print(count)    
count = 1
while count < 11:
    if count == 8:
        break  # break at 8
    print(count)
    count += 1