# filename: plot_stocks.py
import matplotlib.pyplot as plt
import pandas as pd
from pandas_datareader import data as pdr

# 设置绘图样式为默认
plt.style.use('default')

# 获取股票数据的函数
def fetch_stock_data(stock_ticker, start_date, end_date):
    """利用 pandas_datareader 从 Yahoo 财经获取股票数据"""
    return pdr.get_data_yahoo(stock_ticker, start=start_date, end=end_date)

# 定义日期范围
start_date = '2024-01-01'
end_date = '2024-06-30'

# 获取数据
nvda_data = fetch_stock_data('NVDA', start_date, end_date)
tsla_data = fetch_stock_data('TSLA', start_date, end_date)

# 计算相对于年初的收益
nvda_returns = (nvda_data['Close'] / nvda_data['Close'].iloc[0] - 1) * 100
tsla_returns = (tsla_data['Close'] / tsla_data['Close'].iloc[0] - 1) * 100

# 绘图
plt.figure(figsize=(10, 5))
plt.plot(nvda_returns, label='NVDA')
plt.plot(tsla_returns, label='TSLA')
plt.title('YTD Stock Gains for NVDA and TSLA (2024)')
plt.xlabel('Date')
plt.ylabel('Return (%)')
plt.legend()
plt.grid(True)

# 保存图表
plt.savefig('ytd_stock_gains.png')
plt.show()
