# filename: fetch_and_plot_stocks.py
from functions import get_stock_prices, plot_stock_prices

# Define the stock symbols and the date range for YTD
stock_symbols = ['NVDA', 'TSLA']
start_date = '2024-01-01'
end_date = '2024-06-30'

# Fetch the stock prices YTD for NVDA and TSLA
stock_prices = get_stock_prices(stock_symbols, start_date, end_date)

# Plot the stock prices and save to a file
filename = 'stock_prices_YTD_plot.png'
plot_stock_prices(stock_prices, filename)

print(f"Stock prices plotted and saved in {filename}")