# filename: nvidia_stock_analysis.py

import yfinance as yf
import matplotlib.pyplot as plt

# Fetch data again
nvidia = yf.Ticker("NVDA")
data = nvidia.history(start="2024-03-23", end="2024-04-24")
prices = data['Close']

# Calculate metrics
highest_price = prices.max()
lowest_price = prices.min()
price_change = prices.iloc[-1] - prices.iloc[0]

# Output the metrics
print(f"Highest Price: {highest_price}")
print(f"Lowest Price: {lowest_price}")
print(f"Price Change: {price_change} from March 23, 2024, to April 23, 2024")

# Plotting the stock prices
plt.figure(figsize=(10, 5))
plt.plot(prices.index, prices.values, marker='o', linestyle='-')
plt.title('Nvidia Stock Price from March 23 to April 23, 2024')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.grid(True)
plt.show()
