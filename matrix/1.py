# Create an empty 3x3 matrix
matrix = []

# Input the matrix elements
print("Enter elements of 3x3 matrix:")
for i in range(3):
    row = []
    for j in range(3):
        element = int(input(f"Element [{i}][{j}]: "))
        row.append(element)
    matrix.append(row)
    
print("\nThe 3x3 matrix is:")
for row in matrix:
    for element in row:
        print(element, end="\t")
    print()
