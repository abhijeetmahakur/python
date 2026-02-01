import numpy as np

sugar = np.array([85, 110, 145, 95, 130, 160])

result = np.empty(sugar.shape, dtype=object)

result[sugar < 100] = "Normal"
result[(sugar >= 100) & (sugar <= 139)] = "Pre-Diabetic"
result[sugar >= 140] = "Diabetic"

print("Blood Sugar:", sugar)
print("Condition:", result)
