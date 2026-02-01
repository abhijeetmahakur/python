matrix1 = []
print("Enter elements of the first 3x3 matrix:")
for i in range(3):
    row = []
    for j in range(3):
        element = int(input(f"Element [{i}][{j}]: "))
        row.append(element)
    matrix1.append(row)

matrix2 = []
print("\nEnter elements of the second 3x3 matrix:")
for i in range(3):
    row = []
    for j in range(3):
        element = int(input(f"Element [{i}][{j}]: "))
        row.append(element)
    matrix2.append(row)

# Now multiply the two matrices
result = []

for i in range(3):
    row = []
    for j in range(3):
        sum_product = 0
        for k in range(3):
            sum_product += matrix1[i][k] * matrix2[k][j]
        row.append(sum_product)
    result.append(row)

print("\nResult of matrix multiplication:")
for r in result:
    print(r)
