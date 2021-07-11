# 作業目標：練習填入對應的欄位資料或公式, 完成題目的要求
# 作業重點：1.填入適當的輸入資料, 讓後面的程式顯示題目要求的結果 2.填入z轉換的計算方式, 完成轉換後的數值
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_path = 'data/'
df = pd.read_csv(data_path + 'application_train.csv')
print(df.head())

# 將 application_train.csv 中的 CNT_CHILDREN 依照下列規則分為四組，並將其結果在原本的 dataframe 命名為 CNT_CHILDREN_GROUP
# 0 個小孩, 有 1 - 2 個小孩, 有 3 - 5 個小孩, 有超過 5 個小孩
cut_rule = [-np.inf, 0, 2, 5, np.inf]

df['CNT_CHILDREN_GROUP'] = pd.cut(df['CNT_CHILDREN'].values, cut_rule, include_lowest=True)
print(df['CNT_CHILDREN_GROUP'].value_counts())

# 請根據 CNT_CHILDREN_GROUP 以及 TARGET，列出各組的平均 AMT_INCOME_TOTAL，並繪製 baxplot
grp = ['CNT_CHILDREN_GROUP', 'TARGET']
grouped_df = df.groupby(grp)['AMT_INCOME_TOTAL']
print(grouped_df.mean())

plt_column = 'AMT_INCOME_TOTAL'
plt_by = ['CNT_CHILDREN_GROUP', 'TARGET']

df.boxplot(column=plt_column, by = plt_by, showfliers = False, figsize=(12,12))
plt.suptitle('AMT_INCOME_TOTAL')
plt.show()

# 請根據 CNT_CHILDREN_GROUP 以及 TARGET，對 AMT_INCOME_TOTAL 計算 Z 轉換 後的分數
z_score = df['AMT_INCOME_TOTAL_Z_BY_CHILDREN_GRP-TARGET'] = grouped_df.apply(lambda x:(x-np.mean(x))/np.std(x))
print(z_score)