import numpy as np

deg = np.array([0, 30, 45, 60, 90])
rad = np.deg2rad(deg)

print("Degree  Radian   Sin   Cos   Tan")
for i in range(len(deg)):
    print(deg[i], rad[i], np.sin(rad[i]), np.cos(rad[i]), np.tan(rad[i]))
