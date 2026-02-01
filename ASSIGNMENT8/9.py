import numpy as np

arr = np.random.rand(3, 3, 3)

norm = (arr - arr.min()) / (arr.max() - arr.min())
print(norm)
