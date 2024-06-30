# filename: plot_stocks_simulated.py
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 生成模拟数据
np.random.seed(0)
dates = pd.date_range('2024-01-01', '2024-06-30')
nvda_returns = np.cumsum(np.random.randn(len(dates)) / 100.0) * 100
tsla_returns = np.cumsum(np.random.randn(len(dates)) / 100.0) * 100

# 绘图设置
plt.figure(figsize=(10, 5))
plt.plot(dates, nvda_returns, label='NVDA')
plt.plot(dates, tsla_returns, label='TSLA')
plt.title('Simulated YTD Stock Gains for NVDA and TSLA (2024)')
plt.xlabel('Date')
plt.ylabel('Return (%)')
plt.legend()
plt.grid(True)

# 保存图表
plt.savefig('ytd_stock_gains.png')
plt.show()