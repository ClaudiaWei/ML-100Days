# 作業內容：(Kaggle)鐵達尼生存預測¶
# 作業目標：試著完成三種不同特徵類型的三種資料操作, 觀察結果, 哪一種應該最複雜/最難處理
# 作業重點：完成剩餘的八種 類型 x 操作組合, 何種特徵類型最複雜
import pandas as pd
import numpy as np

data_path = 'data/'
df_train = pd.read_csv(data_path + 'titanic_train.csv')
df_test = pd.read_csv(data_path + 'titanic_test.csv')
df_train.shape

# 重組資料成為訓練 / 預測用格式
train_Y = df_train['Survived']
ids = df_test['PassengerId']
df_train = df_train.drop(['PassengerId', 'Survived'] , axis=1)
df_test = df_test.drop(['PassengerId'] , axis=1)
df = pd.concat([df_train,df_test])
print(df.head())

# 秀出資料欄位的類型與數量
dtype_df = df.dtypes.reset_index()
dtype_df.columns = ["Count", "Column Type"]
dtype_df = dtype_df.groupby("Column Type").aggregate('count').reset_index()
print(dtype_df)

#確定只有 int64, float64, object 三種類型後, 分別將欄位名稱存於三個 list 中
int_features = []
float_features = []
object_features = []
for dtype, feature in zip(df.dtypes, df.columns):
    if dtype == 'float64':
        float_features.append(feature)
    elif dtype == 'int64':
        int_features.append(feature)
    else:
        object_features.append(feature)
print(f'{len(int_features)} Integer Features : {int_features}\n')
print(f'{len(float_features)} Float Features : {float_features}\n')
print(f'{len(object_features)} Object Features : {object_features}')

# 整數特徵取平均 (mean), 最大值 (Max), 相異值 (nunique)
print('----int mean----')
print(df[int_features].mean())
print('----int max----')
print(df[int_features].max())
print('----int nunique----')
print(df[int_features].nunique())