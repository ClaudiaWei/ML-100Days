# 作業目標：熟悉更多的 Python 資料操作
# 作業重點：1.列出資料的大小 2.列出所有欄位  3.擷取部分資料
import os
import numpy as np
import pandas as pd

# 設定 data_path
dir_data = './data/'

f_app = os.path.join(dir_data, 'application_train.csv')
print('Path of read in data: %s' % (f_app))
df = pd.read_csv(f_app)
print(df.info())

# 印出前 10 row 資料
print(df.head(n = 10))

# 資料的 row 數以及 column 數
print(df.shape) 

# 列出所有欄位
print(df.columns)

# 截取部分資料
new_df = df.iloc[:8, 0:10] # 前 8 row 以及前 10 個 column
print(new_df)

# TARGET欄位為1
sub_df = df[df.TARGET == 1]
print(sub_df)