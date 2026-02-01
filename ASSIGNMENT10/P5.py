import pandas as pd
import matplotlib.pyplot as plt
population = { 
'Year': [2006,2007,2008,2009,2010],'Region A': [50, 52, 54, 56, 58],'Region B': [40, 42, 44, 47, 49] } 
df = pd.DataFrame(population) 
print(df) 
plt.plot(df['Year'], df['Region A'], label='Region A') 
plt.plot(df['Year'], df['Region B'], label='Region B') 
plt.legend() 
plt.title("Population Growth Comparison",color="teal",fontweight="bold") 
plt.xlabel("Year",fontweight="bold",fontstyle="italic") 
plt.ylabel("Population (Millions)",fontweight="bold",fontstyle="italic") 
plt.show()