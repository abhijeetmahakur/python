import pandas as pd
import matplotlib.pyplot as plt
covid = { 'Day': [1,2,3,4,5], 'Confirmed': [100, 150, 200, 250, 300],'Recovered': [20, 50, 80, 120, 160] } 
df = pd.DataFrame(covid) 
print(df) 
plt.plot(df['Day'], df['Confirmed'], label='Confirmed') 
plt.plot(df['Day'], df['Recovered'], label='Recovered') 
plt.legend() 
plt.title("COVID-19 Trends",color="teal",fontweight="bold") 
plt.xlabel("Day",fontweight="bold",fontstyle="italic") 
plt.ylabel("Cases",fontweight="bold",fontstyle="italic") 
plt.show()