#Line
from matplotlib import pyplot as plt

x = [i for i in range(20)]
y = [6,19,2,14,15,11,9,9,12,4,8,6,16,27,12,8,17,10,9,17] 
plt.title("India VS South Africa(Batting India)", fontsize=15, fontweight='bold', color='maroon')
plt.xlabel("Overs", fontsize=15, fontstyle='italic', color="black")
plt.ylabel("Score", fontsize=15, fontstyle='italic', color='black')
plt.plot(x, y, marker='o')
plt.show()