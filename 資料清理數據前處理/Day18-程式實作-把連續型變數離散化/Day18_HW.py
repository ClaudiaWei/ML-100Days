# 作業目標：使用 Day 17 剛學到的方法, 對較完整的資料(application_train.csv)生成離散化特徵
# 作業重點：1.將年齡資料 ('DAYS_BIRTH' 除以 365) 離散化 2.製上述的 "離散化標籤" 與目標值 ('TARGET') 的長條圖
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
df.head()

# 受雇日數為異常值的資料, 另外設一個欄位記錄, 並將異常的日數轉成空值 (np.nan)
df['DAYS_EMPLOYED_ANOM'] = df["DAYS_EMPLOYED"] == 365243
df['DAYS_EMPLOYED'].replace({365243: np.nan}, inplace = True)

# 出生日數 (DAYS_BIRTH) 取絕對值 
df['DAYS_BIRTH'] = abs(df['DAYS_BIRTH'])

# 連續型特徵離散化
age_data = df[['TARGET', 'DAYS_BIRTH']]
age_data['YEARS_BIRTH'] = age_data['DAYS_BIRTH'] / 365

# 將年齡分組
age_data['YEARS_BINNED'] = pd.cut(age_data['YEARS_BIRTH'], bins = np.linspace(20, 70, num = 11))
print(age_data.head(10))

# 計算平均值
age_groups  = age_data.groupby('YEARS_BINNED').mean()
print(age_groups)

# 繪製目標值平均與分組組別的長條圖
plt.bar(range(len(age_groups.index)), age_groups['TARGET'])
