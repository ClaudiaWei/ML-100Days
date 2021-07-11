# 教學目標：用統計值與圖形觀察可能的離群值
# 範例重點：1.觀察離群值 2.將疑似離群值的資料移除後, 看看剩餘的資料是否正常 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_path = './data/'
df = pd.read_csv(data_path + 'application_train.csv')
print(df.head())

# 檢視不同欄位是否有異常值
# DAYS_BIRTH：客戶申請貸款時的年齡
print((df['DAYS_BIRTH'] / (-365)).describe())

# DAYS_EMPLOYED：申請貸款前，申請人已在現職工作的時間
print((df['DAYS_EMPLOYED'] / 365).describe())
plt.hist(df['DAYS_EMPLOYED'])
plt.show()
print(df['DAYS_EMPLOYED'].value_counts())

# 從上面的圖與數值觀察到 365243 顯然是個奇怪的數值
anom = df[df['DAYS_EMPLOYED'] == 365243]
non_anom = df[df['DAYS_EMPLOYED'] != 365243]
print('The non-anomalies default on %0.2f%% of loans' % (100 * non_anom['TARGET'].mean()))
print('The anomalies default on %0.2f%% of loans' % (100 * anom['TARGET'].mean()))
print('There are %d anomalous days of employment' % len(anom))

print(sum(df['DAYS_EMPLOYED'] == 365243)/len(df))

# 新增一個欄位：DAYS_EMPLOYED_ANOM 來標記 DAYS_EMPLOYED 是否異常
df['DAYS_EMPLOYED_ANOM'] = df["DAYS_EMPLOYED"] == 365243
print(df['DAYS_EMPLOYED_ANOM'].value_counts())

# 這邊我們用 nan 將異常值取代
df['DAYS_EMPLOYED'].replace({365243: np.nan}, inplace = True)
df['DAYS_EMPLOYED'].plot.hist(title = 'Days Employment Histogram')
plt.xlabel('Days Employment')

# 檢查 OWN_CAR_AGE：貸款人的車齡
plt.hist(df[~df.OWN_CAR_AGE.isnull()]['OWN_CAR_AGE'])
plt.show()
df['OWN_CAR_AGE'].value_counts()
df[df['OWN_CAR_AGE'] > 50]['OWN_CAR_AGE'].value_counts()

# 從上面發現車齡為 64, 65 的人特別多
print("Target of OWN_CAR_AGE >= 50: %.2f%%" % (df[df['OWN_CAR_AGE'] >= 50 ]['TARGET'].mean() * 100 ))
print("Target of OWN_CAR_AGE < 50: %.2f%%" % (df[df['OWN_CAR_AGE'] < 50]['TARGET'].mean() * 100))