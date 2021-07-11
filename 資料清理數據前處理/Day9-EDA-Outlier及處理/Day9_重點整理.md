# Day9-EDA:Outlier及處理重點整理
## 知識點目標
1. 了解什麼是例外值 (outlier)
2. 學會如何透過資料探勘方法找到例外值

### Outliers 介紹
- 異常值 (Outliers) 出現的可能原因
    - 所有未知值，隨意填補 (約定俗成的代入) 如年齡 = -1 或 999, 電話是 0900-123-456
    - 可能的錯誤紀錄/手誤/系統性錯誤 如某本書在某筆訂單的銷售量 = 1000 本
- 檢查 Outliers 的流程與方法
    - 盡可能確認每一個欄位的意義
    - 透過檢查數值範圍或繪製散點圖、分布圖或其他圖形檢查是否有異常。
- 對 Outliers 的處理方法
    - 新增欄位用以紀錄異常與否
    - 填補 (取代)
    - 視情況以中位數, Min, Max 或平均數填補(有時會用 NA)

## 知識點複習
1. 檢查異常值的方法
    - 統計值：如平均數、標準差、中位數、分位數
    - 畫圖：如直方圖、盒圖、次數累積分布等
2. 處理異常值
    - 取代補值：中位數、平均數等
    - 另建欄位
    - 整欄不用

## 延伸閱讀
1. [Ways to Detect and Remove the Outliers](https://towardsdatascience.com/ways-to-detect-and-remove-the-outliers-404d16608dba)
    - 視覺方法：boxplot, scatter plot
    - 統計方法：zscore, IQR

2. [How to Use Statistics to Identify Outliers in Data](https://machinelearningmastery.com/how-to-use-statistics-to-identify-outliers-in-data/)
- 標準差與容忍範圍
    - 1 個標準差：涵蓋 68% 數據
    - 2 個標準差：涵蓋 95% 數據
    - 3 個標準差：涵蓋 99.7% 數據
    - 舉例來說，假設一個數字超過平均值 + 3 個標準差，那代表這個樣本點非常罕見! (所以要不是很特別，就是它的發生來自某種問題)