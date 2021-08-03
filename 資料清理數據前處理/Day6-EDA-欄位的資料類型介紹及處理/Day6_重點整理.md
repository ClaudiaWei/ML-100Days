# Day6-EDA：欄位的資料類型介紹及處理
## 知識點目標：
1. 了解 pandas dataframe 欄位的基本資料類型

### 資料類型
#### 資料的欄位變數一般不可分
- 離散變數：只能用整數單位計算的變數
- 連續變數：在一定區間內可以任意取值的變數
#### Pandas DataFrame常見的欄位資料類型
- int64
- float64
- object
- 日期
- boolean

## 知識點複習
1. 拿到資料第一步，通常就是觀察資料有什麼欄位，欄位代表的意義、資料類型是什麼
2. 資料原來是字串/類別的話，如果要做進一步做分析（如訓練模型），一般需要轉為數值的資料類型，轉換的方式通常有兩種：
    - **Label encoding**：使用時機通常是該**資料不同類別是有序的**，例如該資料是年齡分組，類別有小孩、年輕人、老人，表示為 0, 1, 2 是合理的，因為年齡上老人 > 年輕人、年輕人 > 小孩
    - **One Hot encoding**：使用時機通常是該**資料不同類別是無序的**，例如國家

## 延伸閱讀
[Label Encoder vs. One Hot Encoder in Machine Learning](https://contactsunny.medium.com/label-encoder-vs-one-hot-encoder-in-machine-learning-3fc273365621)
- 閱讀重點整理：
    - Label encoding: 把每個類別 mapping 到某個整數，不會增加新欄位
        - 運行這段程式碼後，若查看 x 的值，會看到第一列中的三個國家已被 0、1 和 2 替換。
        > from sklearn.preprocessing import LabelEncoder
        labelencoder = LabelEncoder()
        x[:, 0] = labelencoder.fit_transform(x[:, 0]) 
        - 然而有個問題產生，若將一組國家名稱編碼為數字，這實際上是分類數據，row之間沒有任何關係。為了克服此問題，我們使用One Hot encoding
    - One Hot encoding: 為每個類別新增一個欄位，用 0/1 表示是否 
        - 運行這段程式碼後，指定哪一列必須是one hot encoded，在此範例為[0]。
        > from sklearn.preprocessing import OneHotEncoder
        onehotencoder = OneHotEncoder(categorical_features = [0])
        x = onehotencoder.fit_transform(x).toarray()