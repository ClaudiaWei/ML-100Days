# 教學目標：初步熟悉以 Python 為主的資料讀取與簡單操作
# 範例重點：1.如何使用 pandas.read_csv 讀取資料 2.如何簡單瀏覽 pandas 讀進的資料
import os
import numpy as np
import pandas as pd

# 設定 data_path
dir_data = './data/'

# 讀取資料
f_app = os.path.join(dir_data, 'application_train.csv')
print('Path of read in data: %s' % (f_app))
df = pd.read_csv(f_app)
print(df.head())