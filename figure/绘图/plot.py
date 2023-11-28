import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import FuncFormatter
from matplotlib.dates import date2num
import os

# 设置中文字体为宋体（SimSun）
plt.rcParams['font.sans-serif']=['STSong']     # 中文宋体
# 设置英文字体为 Times New Roman
plt.rcParams['font.serif'] = 'Times New Roman'
# 设置显示负号
plt.rcParams['axes.unicode_minus'] = False
# 设置全局字体大小
plt.rcParams.update({'font.size': 15})

def format_large_number(number, _):
    if abs(number) >= 1e12:
        return "{:.0f} t".format(number / 1e12)
    elif abs(number) >= 1e9:
        return "{:.0f} b".format(number / 1e9)
    elif abs(number) >= 1e6:
        return "{:.0f} m".format(number / 1e6)
    else:
        return "{:,.0f}".format(number)
    
def plot_nn_size():
    # 两个年月时间
    start_date = pd.to_datetime('2018-01-01')
    end_date = pd.to_datetime('2021-02-01')
    date_range = pd.date_range(start_date, end_date, freq='6M')
    date = [pd.to_datetime('2018-01'),pd.to_datetime('2018-06'),pd.to_datetime('2018-10'),pd.to_datetime('2019-01'),pd.to_datetime('2019-02'),pd.to_datetime('2019-03'),pd.to_datetime('2019-06'),pd.to_datetime('2019-06'),pd.to_datetime('2019-06'),pd.to_datetime('2019-07'),pd.to_datetime('2019-08'),pd.to_datetime('2019-08'),pd.to_datetime('2020-02'),pd.to_datetime('2020-05'),pd.to_datetime('2020-06'),pd.to_datetime('2021-01')]
    size = [9.4e7,1.1e8,3.4e8,4.56e8,1.5e9,3.3e8,3.4e8,6.65e8,1.5e9,3.55e8,8.3e9,6.6e7,1.7e10,1.75e11,6.0e11,1.6e12]
    plt.figure(figsize=(9, 6.3))
    # 绘制散点图
    plt.scatter(date, size, color='blue', marker='o', label='Data Points')
    plt.ylabel('参数量')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.yscale('log')
    plt.xticks(date_range, [date.strftime('%Y-%m') for date in date_range], rotation=0)
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_large_number))
    plt.tight_layout()
    dir = os.path.dirname(os.path.abspath(__file__))
    plt.savefig(os.path.join(dir, 'nn_params.svg'), format='svg')
    plt.show()

if __name__ == '__main__':
    plot_nn_size()