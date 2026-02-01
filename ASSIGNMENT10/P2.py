import pandas as pd 
import matplotlib.pyplot as plt 
data = {'Day': ['Mon','Tue','Wed','Thu','Fri'],'Temperature': [30, 32, 31, 33, 34]} 
df = pd.DataFrame(data) 
print(df) 
plt.plot(df['Day'], df['Temperature']) 
plt.title("Daily Temperature Trend",color="red",fontweight="bold") 
plt.xlabel("Day") 
plt.ylabel("Temperature (°C)") 
plt.show()