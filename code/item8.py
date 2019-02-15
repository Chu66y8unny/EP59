matrix = [[1, 2, 3], [4, 5, 6]]

# flat matrix to a list by row
# by plain loops
vec_by_row = []
for row in matrix:
    for col in row:
        vec_by_row.append(col)
print(vec_by_row)
# by list comprehension
vec_by_row.clear()
vec_by_row = [x for row in matrix for x in row]
print(vec_by_row)

# flat matrix to a list by col
# by plain loops
vec_by_col = []
for ci in range(len(matrix[0])):
    for row in matrix:
        vec_by_col.append(row[ci])
print(vec_by_col)
# by list comprehension
vec_by_col.clear()
vec_by_col = [row[ci] for ci in range(len(matrix[0])) for row in matrix]
print(vec_by_col)

# Matrix transpose
t = [[row[ci] for row in matrix] for ci in range(len(matrix[0]))]
print(t)

# Create 2-D Matrix with * operator
m = [[0] * 4] * 3
print(m)
# Gotcha: it created one row and created three references to it
# row = [0] * 4
# m = [row, row, row]
assert m[0] is m[1] and m[1] is m[2]
# Solution: name = [[val] * cols for i in range(rows)]
# m = []
# for i in range(rows):
#     m.append([val] * cols)


