
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
# import xlwt
# import xlrd
import pandas as pd

# def get_y(x):
#     return 0.013*x*x + 0.7796*x + 314.73


# for i in range(1, 144):
#     print(get_y(i))


# 全球二氧化碳浓度历史曲线
# https://www.bilibili.com/video/av851656662/?vd_source=0f445366e59de7d53317c1b976e6aee6

# Python实现——二次多项式回归(最小二乘法)
# https://www.cnblogs.com/LOSKI/p/10639621.html

# 基于tensorflow的一元二次方程回归预测
# https://cloud.tencent.com/developer/article/1351813


# 使用sklearn进行线性回归和二次回归的比较
# https://www.cnblogs.com/cxq1126/p/13042046.html

# python数据处理三：使用sklearn实现曲线拟合
# https://blog.csdn.net/qq_39507748/article/details/110695417

# 使用sklearn库做线性回归拟合
# https://zhuanlan.zhihu.com/p/70679096

# 多项式最小二乘法拟合的python代码实现
# https://zhuanlan.zhihu.com/p/262254688


# 基于Tensorflow 三层神经网络拟合二次函数（附代码与解析）
# https://blog.csdn.net/abc123mma/article/details/109092071

# Linear and Non-Linear Trendlines in Python
# https://plotly.com/python/linear-fits/

df = pd.read_excel('2022_HiMCM_Data-B-co2.xlsx')
# print(df.Year)
# print(df.PPM)


cols1 = df.Year  # 获取第一列
cols2 = df.PPM  # 获取第二列
# print(cols1[0])
# print(cols2[0])

n = 63
s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0
s6 = 0
s7 = 0
for i in range(n):
    s1 = s1+cols2[i]
    s2 = s2+cols1[i]
    s3 = s3+cols1[i]*cols1[i]
    s4 = s4+cols1[i]*cols2[i]
    s5 = s5+cols1[i]*cols1[i]*cols1[i]
    s6 = s6+cols1[i]*cols1[i]*cols2[i]
    s7 = s7+cols1[i]*cols1[i]*cols1[i]*cols1[i]
b0 = sp.Symbol('b0')
b1 = sp.Symbol('b1')
b2 = sp.Symbol('b2')
f1 = ((s1-b1*s2-b2*s3)/100)-b0
f2 = ((s4-b0*s2-b2*s5)/s3)-b1
f3 = ((s6-b0*s3-b1*s5)/s7)-b2
result = sp.solve([f1, f2, f3], [b0, b1, b2])

#{b0: 5.54334244651814, b1: 0.458746450400443, b2: 0.960930395945233}

# b0=sp.Symbol('b0')
# b1=sp.Symbol('b1')
# b2=sp.Symbol('b2')
# sp.solve([((s1-b1*s2-b2*s3)/100)-b0,((s4-b0*s2-b2*s5)/s3)-b1,((s6-b0*s3-b1*s5)/s7)-b2],[b0,b1,b2])
a = result[b0]
b = result[b1]
c = result[b2]
print(c)
print(b)
print(a)
plt.scatter(cols1, cols2, color='blue')
x = np.linspace(1959, 11000, 11000-1959+1)
print(x)
y = a+b*x+c*x*x
# plt.plot(x, y, color="red")


xx = np.linspace(0, 96, 96-0+1)
yy = 0.013*xx*xx + 0.7796*xx + 314.73
plt.plot(xx+1958, yy, color="red")

plt.show()
print(a+b*2050+c*2050*2050)

print(a+b*2100+c*2100*2100)
