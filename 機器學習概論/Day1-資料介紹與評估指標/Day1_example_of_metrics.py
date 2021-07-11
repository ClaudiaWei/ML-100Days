'''
統計指標實作範例
[教學目標]
開始的第一堂課：我們先一些機器學習的基礎開始, 需要用到一些 Python 語法
如果不熟 Python, 但是至少熟悉過一門語言, 可以從這些範例開始熟悉
所謂評價函數 (Metric), 就是機器學習的計分方式, 範例會展示平均絕對誤差 (MAE) 的寫法
我們來了解意義並寫作一個函數吧!!
[範例重點]
複習 / 熟悉 Python 載入套件的語法, 了解什麼是代稱
了解 Python 如何使用 Numpy 套件, 計算我們所需要的數值與繪圖
如何寫作平均絕對誤差 (MAE) 函數
'''
import numpy as np
import matplotlib.pyplot as plt

w = 3
b = 0.5

x_lin = np.linspace(0, 100, 101)
print(x_lin) # Array

y = (x_lin + np.random.randn(101) * 5) * w + b
print(y) # Array

plt.plot(x_lin, y, 'b.', label = 'data points')
plt.title("Assume we have data points")
plt.legend(loc = 2)
plt.show()

y_hat = x_lin * w + b
plt.plot(x_lin, y, 'b.', label = 'data')
plt.plot(x_lin, y_hat, 'r-', label = 'prediction')
plt.title("Assume we have data points (And the prediction)")
plt.legend(loc = 2)
plt.show()

def mean_absolute_error(y, yp):
    mae = MAE = sum(abs(y - yp)) / len(y)
    return mae

MAE = mean_absolute_error(y, y_hat)
print("The Mean absolute error is %.3f" % (MAE))

