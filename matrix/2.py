#wap to input two matrixa and perform its addition
# Input matrix
matrix1 = []
print("Enter elements of the first 3x3 matrix:")
for i in range(3):
    row = []
    for j in range(3):
        element = int(input(f"Element [{i}][{j}]: "))
        row.append(element)
    matrix1.append(row)

# Inputsecond matrix
matrix2 = []
print("\nEnter elements of the second 3x3 matrix:")
for i in range(3):
    row = []
    for j in range(3):
        element = int(input(f"Element [{i}][{j}]: "))
        row.append(element)
    matrix2.append(row)

# Add the two matrices
result = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

# Display the result
print("\nResultant Matrix after addition:")
for row in result:
    for element in row:
        print(element, end="\t")
    print()

