import numpy as np

v1 = np.random.randint(1, 10, (2, 2))
v2 = np.random.randint(1, 10, (2, 2))

print("v1:\n", v1)
print("v2:\n", v2)

len_v1 = np.linalg.norm(v1)
len_v2 = np.linalg.norm(v2)

print("Length of v1:", len_v1)
print("Length of v2:", len_v2)

v1Norm = v1 / len_v1
v2Norm = v2 / len_v2

print("Normalized v1:\n", v1Norm)
print("Normalized v2:\n", v2Norm)

dot = np.sum(v1 * v2)
angle_rad = np.arccos(dot / (len_v1 * len_v2))
angle_deg = np.degrees(angle_rad)

print("Angle (radian):", angle_rad)
print("Angle (degree):", angle_deg)
