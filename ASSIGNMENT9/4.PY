import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 50)

plt.plot(x, np.sin(x), label="Sine")
plt.plot(x, np.cos(x), label="Cosine")
plt.plot(x, np.tan(x), label="Tangent")

plt.legend()
plt.title("Trigonometric Functions")
plt.show()
