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