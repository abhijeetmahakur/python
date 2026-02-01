import numpy as np
import random
import time

# NumPy method
start = time.time()
arr1 = np.random.random((1000, 1000))
end = time.time()
numpy_time = end - start

# Python loop method
start = time.time()
arr2 = [[random.random() for _ in range(1000)] for _ in range(1000)]
end = time.time()
python_time = end - start

print("NumPy Time:", numpy_time)
print("Python Loop Time:", python_time)

if numpy_time < python_time:
    print("NumPy is faster")
else:
    print("Python loop is faster")
