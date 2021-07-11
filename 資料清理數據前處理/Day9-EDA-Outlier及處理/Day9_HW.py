# 作業目標：依照下列提示與引導, 以幾種不同的方式, 檢視可能的離群值
# 作業重點：1.從原始資料篩選可能的欄位, 看看那些欄位可能有離群值 2.繪製目標值累積密度函數(ECDF)的圖形, 和常態分布的累積密度函數對比, 以確認是否有離群值的情形
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_path = './data/'
df = pd.read_csv(data_path + 'application_train.csv')
print(df.head())

## 請參考 HomeCredit_columns_description.csv 的欄位說明，觀察並列出三個你覺得可能有 outlier 的欄位並解釋可能的原因
# 先篩選數值型的欄位
dtype_select = []
numeric_columns = list(df.columns[list(df.dtypes.isin(dtype_select))])

# 再把只有 2 值 (通常是 0,1) 的欄位去掉
numeric_columns = list(df[numeric_columns].columns[list(df[numeric_columns].apply(lambda x:len(x.unique())!=2 ))])
print("Numbers of remain columns: %i" % len(numeric_columns))

# 檢視這些欄位的數值範圍
for i in numeric_columns:
    print(df.boxplot(i))
    plt.show()

a = df['OWN_CAR_AGE'].dropna()
print(plt.hist(a))

# 從上面的圖檢查的結果，至少這三個欄位好像有點可疑：AMT_INCOME_TOTAL, REGION_POPULATION_RELATIVE, OBS_60_CNT_SOCIAL_CIRCLE
# 最大值離平均與中位數很遠
print(df['AMT_INCOME_TOTAL'].describe())

# 繪製 Empirical Cumulative Density Plot (ECDF)
cdf = df.AMT_INCOME_TOTAL.value_counts().sort_index().cumsum()
plt.plot(list(cdf.index), cdf/cdf.max())
plt.xlabel('Value')
plt.ylabel('ECDF')
plt.xlim([cdf.index.min(), cdf.index.max() * 1.05]) # 限制顯示圖片的範圍
plt.ylim([-0.05,1.05]) # 限制顯示圖片的範圍
plt.show()

# 改變 y 軸的 Scale, 正常檢視 ECDF
plt.plot(np.log(list(cdf.index)), cdf/cdf.max())
plt.xlabel('Value (log-scale)')
plt.ylabel('ECDF')
plt.ylim([-0.05,1.05]) # 限制顯示圖片的範圍
plt.show()

# 最大值落在分布之外
print(df['REGION_POPULATION_RELATIVE'].describe())

# 繪製 Empirical Cumulative Density Plot (ECDF)
cdf = df.REGION_POPULATION_RELATIVE.value_counts().sort_index().cumsum()
plt.plot(list(cdf.index), cdf/cdf.max())
plt.xlabel('Value')
plt.ylabel('ECDF')
plt.ylim([-0.05,1.05]) # 限制顯示圖片的範圍
plt.show()
df['REGION_POPULATION_RELATIVE'].hist()
plt.show()
df['REGION_POPULATION_RELATIVE'].value_counts()

# 最大值落在分布之外
print(df['OBS_60_CNT_SOCIAL_CIRCLE'].describe())

# 繪製 Empirical Cumulative Density Plot (ECDF)
cdf = df.OBS_60_CNT_SOCIAL_CIRCLE.value_counts().sort_index().cumsum()
plt.plot(list(cdf.index), cdf/cdf.max())
plt.xlabel('Value')
plt.ylabel('ECDF')
plt.xlim([cdf.index.min() * 0.95, cdf.index.max() * 1.05])
plt.ylim([-0.05,1.05])
plt.show()
df['OBS_60_CNT_SOCIAL_CIRCLE'].hist()
plt.show()
print(df['OBS_60_CNT_SOCIAL_CIRCLE'].value_counts().sort_index(ascending = False))
