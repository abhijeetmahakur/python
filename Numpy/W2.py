import numpy as np
from matplotlib import  pyplot as plt
x = [0,30,45,60,75,90]
y = np.sin(radians(x))
plt.title("Sine Graph", fontsize=15, fontweight='bold', color='maroon')
plt.xlabel("Degrees", fontsize=15, fontstyle='italic', color="black")
plt.ylabel("trigonometric value", fontsize=15, fontstyle='italic', color='black')
plt.plot(x,y)
plt.show()