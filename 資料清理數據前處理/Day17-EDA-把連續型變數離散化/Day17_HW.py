# 作業目標：熟悉查詢函數的方法與理解參數性質, 並了解數值的離散化的調整工具
# 作業重點：設定 pd.cut 的參數以指定間距, 新增一個欄位 customized_age_grp，把 age 分為 (0, 10], (10, 20], (20, 30], (30, 50], (50, 100] 這五組
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 初始設定 Ages 的資料
ages = pd.DataFrame({"age": [18,22,25,27,7,21,23,37,30,61,45,41,9,18,80,100]})

# 新增欄位 "equal_width_age", 對年齡做等寬劃分
ages["equal_width_age"] = pd.cut(ages["age"], 4)

# 觀察等寬劃分下, 每個種組距各出現幾次
ages["equal_width_age"].value_counts() # 每個 bin 的值的範圍大小都是一樣的

# 新增欄位 "equal_freq_age", 對年齡做等頻劃分
ages["equal_freq_age"] = pd.qcut(ages["age"], 4)

# 觀察等頻劃分下, 每個種組距各出現幾次
ages["equal_freq_age"].value_counts() # 每個 bin 的資料筆數是一樣的

# 新增一個欄位 customized_age_grp, 並指定劃分區間
ages['customized_age_grp'] = pd.cut(ages["age"], [0, 10, 20, 30, 50, 100])
print(ages)



