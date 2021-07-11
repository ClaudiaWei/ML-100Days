# Day11-常用的數值取代：中位數與分位數連續數值標準化重點整理
## 知識點目標
1. 如何處理例外值
2. 如何進行數據標準化

### 常用以填補的統計值
- 中位數：np.median(value_array)
- 分位數：np.quantile(value_array, q = ....)
- 眾數：dictionary method(較快的方法)、scipy.stats.mode(value_array)
- 平均數：np.mean(value_array)

### 連續型數值標準化
- 為何要標準化：改變1單位x對應y的影響
- 是否一定要標準化：根據使用的模型而定
    - Regression model：有差
    - Tree-based model：沒有太大關係

### 常用的標準化方法
- Z轉換
- 空間壓縮

## 知識點複習
1. 運用統計值處理例外狀況
2. 是否標準化依據模型、演算法、指標等等而定

## 延伸閱讀
無