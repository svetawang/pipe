# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


import re
import numpy
import matplotlib.pyplot as plt
import linecache
import decimal

import numpy as np


def readarray(file, colour, label):
    data_x = []
    data_y = []
    for i in range(30, 1229):
        data = linecache.getline(file, i)
        temp = data.strip().split(',', 1)
        temp_x = decimal.Decimal(temp[0])
        temp_y = decimal.Decimal(temp[1])
        data_x.append(temp_x)
        data_y.append(temp_y)
    plt.plot(data_x, data_y, color=colour, label=label)


if __name__ == '__main__':
    fig1 = plt.figure(figsize=(8, 8), dpi=200)
    readarray(file='v0.01.txt', colour='blue', label='v=0.01')
    readarray(file='v0.02.txt', colour='green', label='v=0.02')
    readarray(file='v0.04.txt', colour='purple', label='v=0.04')
    readarray(file='v0.06.txt', colour='red', label='v=0.06')
    readarray(file='v0.08.txt', colour='yellow', label='v=0.08')
    readarray(file='v0.10.txt', colour='black', label='v=0.10')
    plt.xlabel('Potential/V')
    plt.ylabel('Current/A')
    plt.title('V-A curve,v change')
    plt.legend()
    plt.savefig('v-curve.png')

    fig2 = plt.figure(figsize=(8, 8), dpi=200)
    readarray(file='c0.5.txt', colour='blue', label='c=0.5')
    readarray(file='c1.0.txt', colour='green', label='c=1.0')
    readarray(file='c2.0.txt', colour='purple', label='c=2.0')
    readarray(file='c4.0.txt', colour='red', label='c=4.0')
    plt.xlabel('Potential/V')
    plt.ylabel('Current/A')
    plt.title('V-A curve,v change')
    plt.legend()
    plt.savefig('c-curve.png')
    plt.show()
