import yfinance as yf 
import matplotlib.pyplot as plt 
stock1 = yf.download("AAPL", start="2024-01-01", end="2024-03-01") 
stock2 = yf.download("MSFT", start="2024-01-01", end="2024-03-01") 
print(stock1.head()) 
plt.plot(stock1['Close'], label='Apple') 
plt.plot(stock2['Close'], label='Microsoft') 
plt.title("Stock Closing Prices",color="maroon",fontweight="bold") 
plt.xlabel("Date") 
plt.ylabel("Price") 
plt.legend() 
plt.show()