# 作業目標：使用 pandas.corr() 函數顯示相關係數並加以觀察結果
# 作業重點：結合前幾單元的作法, 試試看是否能夠用繪圖顯示出特徵與目標的相關性
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

data_path = './data/'
df = pd.read_csv(data_path + 'application_train.csv')
print(df.head())

# 將只有兩種值的類別型欄位, 做 Label Encoder, 計算相關係數時讓這些欄位可以被包含在內
le = LabelEncoder()

# 檢查每一個 column
for col in df:
    if df[col].dtype == 'object':
        # 如果只有兩種值的類別型欄位
        if len(list(df[col].unique())) <= 2:
            # 就做 Label Encoder, 以加入相關係數檢查
            df[col] = le.fit_transform(df[col])            
print(df.shape)
print(df.head())

# 受雇日數為異常值的資料, 另外設一個欄位記錄, 並將異常的日數轉成空值 (np.nan)
df['DAYS_EMPLOYED_ANOM'] = df["DAYS_EMPLOYED"] == 365243
df['DAYS_EMPLOYED'].replace({365243: np.nan}, inplace = True)

# 出生日數 (DAYS_BIRTH) 取絕對值 
df['DAYS_BIRTH'] = abs(df['DAYS_BIRTH'])

# 觀察相關係數
print(df.corr()['TARGET'])

correlations = df.corr()['TARGET'].sort_values()
# 顯示相關係數最大 / 最小的各10個欄位名稱
print('Most Positive Correlations:\n', correlations.tail(10))
print('\nMost Negative Correlations:\n', correlations.head(10))