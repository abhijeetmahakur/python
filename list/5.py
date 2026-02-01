import copy

# Original nested list
original = [[1,2,3,4,5,6], [7,8]]

# Shallow copy
shallow = copy.copy(original)

# Deep copy
deep = copy.deepcopy(original)

# Modify the nested list in the shallow copy
shallow[0][0] = '22'

# Modify the nested list in the deep copy
deep[1][1] = '33'

print("Original:", original)
print("Shallow:", shallow)
print("Deep:", deep)
