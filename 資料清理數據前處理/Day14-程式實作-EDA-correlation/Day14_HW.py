# 作業目標：利用 numpy 計算出兩組數據之間的相關係數，並觀察散佈圖
# 作業重點：1.弱相關的相關矩陣 2.正相關的相關矩陣
import numpy as np
import matplotlib.pyplot as plt

print(np.random.seed(1))

# 隨機生成兩組 1000 個介於 0~50 的數的整數 x, y, 看看相關矩陣如何
x = np.random.randint(0, 50, 1000)
y = np.random.randint(0, 50, 1000)

# 呼叫 numpy 裡的相關矩陣函數 (corrcoef)
print(np.corrcoef(x, y))
print(plt.scatter(x, y))

# 隨機生成 1000 個介於 0~50 的數 x
x = np.random.randint(0, 50, 1000)

# 這次讓 y 與 x 正相關，再增加一些雜訊
y = x + np.random.normal(0, 10, 1000)

# 再次用 numpy 裡的函數來計算相關係數
print(np.corrcoef(x, y))
print(plt.scatter(x, y))