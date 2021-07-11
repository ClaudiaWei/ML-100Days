# 作業目標：試著調整資料, 繪製分布圖
# 作業重點：1.如何將列出相異的 HOUSETYPE_MODE 類別 2.如何依照不同的 HOUSETYPE_MODE 類別指定資料, 並繪製長條圖
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns

data_path = './data/'
df = pd.read_csv(data_path + 'application_train.csv')
print(df.head())

# 使用不同的 HOUSETYPE_MODE 類別繪製圖形, 並使用 subplot 排版
unique_house_type = df['HOUSETYPE_MODE'].unique()

nrows = len(unique_house_type)
ncols = nrows // 2

plt.figure(figsize=(8,10))
for i in range(len(unique_house_type)):
    plt.subplot(nrows, ncols, i+1)
    df.loc[df['HOUSETYPE_MODE'] == unique_house_type[i], "AMT_CREDIT"].hist()
    plt.title(str(unique_house_type[i]))
plt.show()    
