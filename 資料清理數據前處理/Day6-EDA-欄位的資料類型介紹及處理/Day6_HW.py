# 作業目標：仿造範例的 One Hot Encoding, 將指定的資料進行編碼
# 作業重點：將 sub_train 進行 One Hot Encoding 編碼
import os
import numpy as np
import pandas as pd

# 設定 data_path, 並讀取 df
data_path = './data/'
df = pd.read_csv(data_path + 'application_train.csv')

# 將下列部分資料片段 sub_train 使用 One Hot encoding, 並觀察轉換前後的欄位數量與欄位名稱變化
sub_train = pd.DataFrame(df['WEEKDAY_APPR_PROCESS_START'])
print(sub_train.shape)
print(sub_train.head())

# One Hot encoding
print('----one hot encoding----')
sub_train = pd.get_dummies(sub_train)
print(sub_train.shape)
print(sub_train.head())
