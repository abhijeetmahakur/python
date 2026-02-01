import matplotlib.pyplot as plt

v1 = [3, 4]
v2 = [4, 2]

plt.quiver(0, 0, v1[0], v1[1], color='green', label='v1')
plt.quiver(0, 0, v2[0], v2[1], color='red', label='v2')

plt.xlim(0,5)
plt.ylim(0,5)
plt.legend()
plt.show()
