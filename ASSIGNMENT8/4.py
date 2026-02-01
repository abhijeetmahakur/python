import numpy as np

temp = np.array([28, 30, 35, 36, 33, 29, 40, 31, 34, 27, 38, 32, 30, 37])
print("Original:", temp)

heat_wave = temp >= 35
print("Heat wave days:", temp[heat_wave])
print("Count:", np.sum(heat_wave))

temp[temp < 30] = 30
print("After replacing <30:", temp)

comfortable = (temp >= 30) & (temp <= 34)
print("Comfortable days:", temp[comfortable])

temp[heat_wave] += 2
print("After correction:", temp)
