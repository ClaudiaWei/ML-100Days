# 作業目標：變項的分群比較, 自 20 到 70 歲，切 11 個點，進行分群比較 (KDE plot), 以年齡區間為 x, target 為 y 繪製 barplot
# 作業重點：如何調整對應資料, 以繪製長條圖
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

data_path = './data/'
df = pd.read_csv(data_path + 'application_train.csv')
print(df.head())

# 資料整理 ( 'DAYS_BIRTH'全部取絕對值 )
df['DAYS_BIRTH'] = abs(df['DAYS_BIRTH'])

# 根據年齡分成不同組別 (年齡區間 - 還款與否)
age_data = df[['TARGET', 'DAYS_BIRTH']] # subset
age_data['YEARS_BIRTH'] = age_data['DAYS_BIRTH'] / 365 # day-age to year-age

#自 20 到 70 歲，切 11 個點 (得到 10 組)
bin_cut =  np.linspace(20, 70, num = 11)
age_data['YEARS_BINNED'] = pd.cut(age_data['YEARS_BIRTH'], bins = bin_cut) 

# 顯示不同組的數量
print(age_data['YEARS_BINNED'].value_counts())
print(age_data.head())

# 繪圖前先排序 / 分組
year_group_sorted = np.sort(age_data['YEARS_BINNED'].unique())
plt.figure(figsize=(8,6))
for i in range(len(year_group_sorted)):
    sns.distplot(age_data.loc[(age_data['YEARS_BINNED'] == year_group_sorted[i]) & \
                              (age_data['TARGET'] == 0), 'YEARS_BIRTH'], label = str(year_group_sorted[i]))
    
    sns.distplot(age_data.loc[(age_data['YEARS_BINNED'] == year_group_sorted[i]) & \
                              (age_data['TARGET'] == 1), 'YEARS_BIRTH'], label = str(year_group_sorted[i]))
plt.title('KDE with Age groups')
plt.show()

# 計算每個年齡區間的 Target、DAYS_BIRTH與 YEARS_BIRTH 的平均值
age_groups  = age_data.groupby('YEARS_BINNED').mean()
print(age_groups)
plt.figure(figsize = (8, 8))

# 以年齡區間為 x, target 為 y 繪製 barplot
px = age_groups.index.astype(str) # 將值強制轉換為dtypes(str)
py = 100 * age_groups['TARGET']
sns.barplot(px, py)

# Plot labeling
plt.xticks(rotation = 75); plt.xlabel('Age Group (years)'); plt.ylabel('Failure to Repay (%)')
plt.title('Failure to Repay by Age Group')