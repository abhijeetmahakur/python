import pandas as pd 
import matplotlib.pyplot as plt 
sales = { 'Month': ['Jan','Feb','Mar','Apr','May'],'Sales': [1000, 1500, 2000, 2800, 3000] } 
df = pd.DataFrame(sales) 
print(df) 
plt.plot(df['Month'], df['Sales']) 
plt.title("<----Monthly Sales Trend---->",color="blue",fontweight="bold") 
plt.xlabel("Month",fontweight="bold") 
plt.ylabel("Sales",fontweight="bold") 
plt.show() 
print("Highest sales month:", df.loc[df['Sales'].idxmax()])