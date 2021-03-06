# Day17-EDA:把連續型變數離散化重點整理
## 知識點目標
1. 了解離散化連續數值的意義以及方法

### 連續型變數離散化
- Goal
    - 變得更簡單 (可能性變少了)
    - 離散化的變數較穩定，假設年齡 > 30是 1，否則 0
- 關鍵點
    - 組的數量：以年齡為例子，每 10 歲一組就會有 10 組
    - 組的寬度：以年齡為例子，一組的寬度是 10 歲
- 主要的方法
    - 等寬劃分：按照相同寬度將資料分成幾等份。缺點是受到異常值的影響比較大
    - 等頻劃分：將資料分成幾等份，每等份資料裡面的個數是一樣的
    - 聚類劃分：使用聚類演算法將資料聚成幾類，每一個類為一個劃分

**除了以上的主要方法，也會因需求而需要自己定義離散化的方式，如何離散化是一門學問！**

## 知識點複習
1. 離散化的目的是讓事情變簡單、減少 outlier 對分析以及訓練模型的影響
2. 主要的方法是等寬劃分 (對應 pandas 中的 cut) 以及等頻劃分 (對應 pandas 中的 qcut)
3. 可以依實際需求來自己定義離散化的方式

## 延伸閱讀
無