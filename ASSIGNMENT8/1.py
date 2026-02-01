import numpy as np

# create random 1-D array
v1 = np.random.randint(1, 50, 10)

print("Array:", v1)

max_val = np.max(v1)
min_val = np.min(v1)

print("Maximum value:", max_val)
print("Minimum value:", min_val)

# count elements between min and max
count = np.sum((v1 >= min_val) & (v1 <= max_val))
print("Elements between min and max:", count)
