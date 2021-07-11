# 範例：(Kaggle)房價預測, 以下用房價預測資料, 觀察特徵的幾種類型，這份資料有 'int64', 'float64', 'object' 三種欄位, 分別將其以python的list格式紀錄下來
# 教學目標：如何將欄位名稱, 依照所屬類型分開, 並列出指定類型的部分資料
# 範例重點：1.如何觀察目前的 DataFrame 中, 有哪些欄位類型, 以及數量各有多少 2.如何將欄位名稱依欄位類型分開 3.如何只顯示特定類型的欄位資料
import pandas as pd
import numpy as np

data_path = 'data/'
df_train = pd.read_csv(data_path + 'house_train.csv')
df_test = pd.read_csv(data_path + 'house_test.csv')
df_train.shape

# 訓練資料需要 train_X, train_Y / 預測輸出需要 ids(識別每個預測值), test_X
# 在此先抽離出 train_Y 與 id, 而先將 train_X, test_X 該有的資料合併成 df, 先作特徵工程
train_Y = np.log1p(df_train['SalePrice']) # log1p是exp(x)的反向-1
ids = df_test['Id']
df_train = df_train.drop(['Id', 'SalePrice'] , axis=1)
df_test = df_test.drop(['Id'] , axis=1)
df = pd.concat([df_train,df_test])
print(df.head())

# 秀出資料欄位的類型, 與對應的數量
# df.dtypes：轉成以欄位為 index, 類別(type)為 value 的 DataFrame
# .reset_index()：預設是將原本的 index 轉成一個新的欄位, 如果不須保留 index, 則通常會寫成 .reset_index(drop=True)
dtype_df = df.dtypes.reset_index() 
dtype_df.columns = ["Count", "Column Type"]
dtype_df = dtype_df.groupby("Column Type").aggregate('count').reset_index()
print(dtype_df)

# 確定只有 int64, float64, object 三種類型後對欄位名稱執行迴圈, 分別將欄位名稱存於三個 list 中
int_features = []
float_features = []
object_features = []
# .dtypes(欄位類型), .columns(欄位名稱) 是 DataFrame 提供的兩個方法, 這裡順便展示一下 for 與 zip 搭配的用法, zip為把多個list的相對應位置鏈起來的函數, 可以將多個迭代器相對應位置打包成元組
for dtype, feature in zip(df.dtypes, df.columns): 
    if dtype == 'float64':
        float_features.append(feature)
    elif dtype == 'int64':
        int_features.append(feature)
    else:
        object_features.append(feature)
# 這邊採用 f-string 的寫法, 如果無法執行, 則需要更新版本或自行將程式改寫為 str.format 形式
print(f'{len(int_features)} Integer Features : {int_features}\n')
print(f'{len(float_features)} Float Features : {float_features}\n')
print(f'{len(object_features)} Object Features : {object_features}')

#單獨秀出特定類型的欄位集合, 方便後續做特徵工程處理
print(df[float_features].head())