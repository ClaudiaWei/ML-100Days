# 作業目標：仿造範例的資料操作, 試著進行指定的離群值處理
# 作業重點：1.計算 AMT_ANNUITY 的分位點 2.將 AMT_ANNUITY 的 NaN 用中位數取代 3.將 AMT_ANNUITY 數值轉換到 -1 ~ 1 之間 4.將 AMT_GOOD_PRICE 的 NaN 用眾數取代
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_path = 'data/'
df = pd.read_csv(data_path + 'house_train.csv')
print(df.head())

# 計算 q0 - q100
q_all = [np.percentile(df[~df['AMT_ANNUITY'].isnull()]['AMT_ANNUITY'], q = i) for i in range(100)]

# 將 NAs 以 q50 填補
print("Before replace NAs, numbers of row that AMT_ANNUITY is NAs: %i" % sum(df['AMT_ANNUITY'].isnull()))
q_50 = np.percentile(df[~df['AMT_ANNUITY'].isnull()]['AMT_ANNUITY'], 50)
df.loc[df['AMT_ANNUITY'].isnull(),'AMT_ANNUITY'] = q_50
print("After replace NAs, numbers of row that AMT_ANNUITY is NAs: %i" % sum(df['AMT_ANNUITY'].isnull()))

# Normalize values to -1 to 1
print("== Original data range ==")
print(df['AMT_ANNUITY'].describe())

def normalize_value(x):
    x = (( (x - min(x)) / ( max(x) - min(x) ) ) - 0.5) * 2
    return x

df['AMT_ANNUITY_NORMALIZED'] = normalize_value(df['AMT_ANNUITY'])
print("== Normalized data range ==")
df['AMT_ANNUITY_NORMALIZED'].describe()

# 列出重複最多的數值
print(df['AMT_GOODS_PRICE'].value_counts().head())
mode_goods_price = list(df['AMT_GOODS_PRICE'].value_counts().index)
df.loc[df['AMT_GOODS_PRICE'].isnull(), 'AMT_GOODS_PRICE'] = mode_goods_price[0]
print("After replace NAs, numbers of row that AMT_GOODS_PRICE is NAs: %i" % sum(df['AMT_GOODS_PRICE'].isnull()))