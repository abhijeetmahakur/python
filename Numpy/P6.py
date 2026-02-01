#import matplotlib.pyplot as pit
from matplotlib import pyplot as plt

x = [10, 20, 30, 40, 50, 60]
y = [5,12,1,3,2,0] 
plt.bar(x, y, marker='o')
plt.title("Line chart", fontsize=15, fontweight='bold', color='maroon')
plt.xlabel("X-axis", fontsize=15, fontstyle='italic', color="black")
plt.ylabel("Y-axis", fontsize=15, fontstyle='italic', color='black')
plt.show()
