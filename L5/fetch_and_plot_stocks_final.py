# filename: fetch_and_plot_stocks_final.py
import time
from functions import get_stock_prices, plot_stock_prices
import pandas as pd

# Define the stock symbols and the date range for YTD
stock_symbols = ['NVDA', 'TSLA']
start_date = '2024-01-01'
end_date = '2024-06-30'

# Retry logic to handle possible operational errors when fetching stock prices
def fetch_stocks_with_retry(symbols, start, end, retries=3, delay=10):
    while retries > 0:
        try:
            stock_prices = get_stock_prices(symbols, start, end)
            print("Stock data fetched successfully.")
            return stock_prices
        except Exception as e:
            print(f"Error fetching stock data: {e}")
            retries -= 1
            time.sleep(delay)  # Wait for some time before retrying
    
    # If all retries fail, return an empty DataFrame
    print("Failed to fetch stock data after several attempts.")
    return pd.DataFrame()

# Fetch the stock prices YTD for NVDA and TSLA with retries
stock_prices = fetch_stocks_with_retry(stock_symbols, start_date, end_date)

# Check if data was fetched
if not stock_prices.empty:
    # Plot the stock prices and save to a file
    filename = 'stock_prices_YTD_plot.png'
    plot_stock_prices(stock_prices, filename)
    print(f"Stock prices plotted and saved in {filename}")
else:
    print("Failed to fetch or plot stock prices due to data retrieval issues.")