# Day13-DataFrame operationData frame merge/常用的DataFrame操作重點整理
## 知識點目標
1. 熟悉 python 常用套件 pandas 的操作方式，如排序、合併、分組操作、Indexing 等

### 轉換與合併 dataframe
- 將欄(column)轉成列(row)：pd.melt(df)
- 將列轉成欄：pd.pivot(columns='var', values='val')
- 沿著列合併兩個dataframe：pd.concat([df1, df2])
- 沿著欄合併兩個dataframe：pd.concat([df1, df2], axis = 1)
- 將df1, df2以'id'這欄做全合併(遺失以na補)：pd.merge(df1, df2, on = 'id', how = 'outer')
- 將df1, df2以'id'這欄做部分合併：pd.merge(df1, df2, on = 'id', how = 'inner')

### Subset
- 列篩選/縮減：
    - 邏輯操作：sub_df = df[df.age > 20]
    - 移除重複：df = df.drop_duplicates()
    - 前n筆：sub_df = df.head(n = 10)
    - 後n筆：sub_df = df.tail(n = 10)
    - 雖機抽樣(10筆)：sub_df = df.sample(n = 10)
    - 第n到m筆：sub_df = df.iloc[n:m]
- 欄篩選/縮減：
    - 單一欄位：new_df = df['col1'] or df.col1
    - 複數欄位：new_df = df[ ['col1', 'col2', 'col3'] ]
    - Regex篩選：new_df = df.filter(regex = .....)

### Group operations
- 計算各組的數量：sub_df_object.size()
- 得到各組的基本統計值：sub_df_object.describe()
- 根據col1分組後，計算col2統計值(以平均值為例)：sub_df_object['col2'].mean()
- 對依col1分組後的col2引用操作：sub_df_object['col2'].apply()
- 對依col1分組後的col2繪圖：sub_df_object['col2'].hist()

## 知識點複習
1. 合併(concat)常用於將多個表依照某欄(key)結合使用
2. 分組(groupby)是常用在計算"組"統計值時會用到的功能
3. 許多基本操作(如 >, ==, <, ~)都是可以在pandas作為篩選條件使用

## 延伸閱讀
1. [Pandas 官方 Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
2. [Pandas Cheat Sheet](https://assets.datacamp.com/blog_assets/PandasPythonForDataScience.pdf)
-  閱讀整理：
    - 實際經驗中使用過將dataframe存入DB：df.to_sql('table_name', engine, if_exists = 'append', index = true)
    - df.iloc：by position, df.loc：by label