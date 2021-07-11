# 教學目標：為了要處理離群值, 我們要先學會計算其他的統計量, 並且還有其他的挑整方式
# 範例重點：1.計算並觀察百分位數 2.計算中位數的方式 3.計算眾數 4.計算標準化與最大最小化
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
from scipy.stats import mode
from collections import defaultdict

data_path = 'data/'
df = pd.read_csv(data_path + 'house_train.csv')
print(df.head())

# 如果欄位中有 NA, describe 會有問題
print(df['AMT_ANNUITY'].describe())

# Ignore NA, 計算五值
five_num = [0, 25, 50, 75, 100]
quantile_5s = [np.percentile(df[~df['AMT_ANNUITY'].isnull()]['AMT_ANNUITY'], q = i) for i in five_num]
print(quantile_5s)

df[~df['AMT_ANNUITY'].isnull()]['AMT_ANNUITY'].hist(bins = 100)
plt.show()

# 試著將 max 取代為 q99
df[df['AMT_ANNUITY'] == df['AMT_ANNUITY'].max()] = np.percentile(df[~df['AMT_ANNUITY'].isnull()]['AMT_ANNUITY'], q = 99)
five_num = [0, 25, 50, 75, 100]
quantile_5s = [np.percentile(df[~df['AMT_ANNUITY'].isnull()]['AMT_ANNUITY'], q = i) for i in five_num]
print(quantile_5s)

# 得到 median 的另外一種方法
np.median(df[~df['AMT_ANNUITY'].isnull()]['AMT_ANNUITY'])

# 計算眾數 (mode)
start_time = time.time()
mode_get = mode(df[~df['AMT_ANNUITY'].isnull()]['AMT_ANNUITY'])
print(mode_get)
print("Elapsed time: %.3f secs" % (time.time() - start_time))

# 計算眾數 (mode)
start_time = time.time()
mode_dict = defaultdict(lambda:0)

for value in df[~df['AMT_ANNUITY'].isnull()]['AMT_ANNUITY']:
    mode_dict[value] += 1
    
mode_get = sorted(mode_dict.items(), key=lambda kv: kv[1], reverse=True)
print(mode_get[0])
print("Elapsed time: %.3f secs" % (time.time() - start_time))

# 以 AMT_CREDIT 為例
df['AMT_CREDIT'].hist(bins = 50)
plt.title("Original")
plt.show()
value = df['AMT_CREDIT'].values

df['AMT_CREDIT_Norm1'] = ( value - np.mean(value) ) / ( np.std(value) )
df['AMT_CREDIT_Norm1'].hist(bins = 50)
plt.title("Normalized with Z-transform")
plt.show()

df['AMT_CREDIT_Norm2'] = ( value - min(value) ) / ( max(value) - min(value) )
df['AMT_CREDIT_Norm2'].hist(bins = 50)
plt.title("Normalized to 0 ~ 1")
plt.show()
