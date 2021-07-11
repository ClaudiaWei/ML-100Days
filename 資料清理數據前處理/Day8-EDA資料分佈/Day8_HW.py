# [作業目標]：對資料做更多處理：顯示特定欄位的統計值與直方圖
# [作業重點]：1. 試著顯示特定欄位的基礎統計數值 2. 試著顯示特定欄位的直方圖
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 設定 data_path
data_path = './data/'
df = pd.read_csv(data_path + 'application_train.csv')
print(df.head())
print(df['AMT_INCOME_TOTAL'].mean())
print(df['AMT_INCOME_TOTAL'].median())
print(df['AMT_INCOME_TOTAL'].hist())
print(plt.xlabel('AMT_INCOME_TOTAL'))