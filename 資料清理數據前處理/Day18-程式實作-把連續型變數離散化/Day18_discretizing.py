# 教學目標：運用 pandas.cut 與 .qcut 計算出數據的離散化標籤
# 範例重點：1.pandas.cut 的等寬劃分效果 2.pandas.qcut 的等頻劃分效果
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 初始設定 Ages 的資料
ages = pd.DataFrame({"age": [18,22,25,27,7,21,23,37,30,61,45,41,9,18,80,100]})
print(ages)

# 新增欄位 "equal_width_age", 對年齡做等寬劃分
ages["equal_width_age"] = pd.cut(ages["age"], 4)

# 觀察等寬劃分下, 每個種組距各出現幾次
print(ages["equal_width_age"].value_counts()) # 每個 bin 的值的範圍大小都是一樣的

# 新增欄位 "equal_freq_age", 對年齡做等頻劃分
ages["equal_freq_age"] = pd.qcut(ages["age"], 4)

# 觀察等頻劃分下, 每個種組距各出現幾次
print(ages["equal_freq_age"].value_counts()) # 每個 bin 的資料筆數是一樣的
print(ages)