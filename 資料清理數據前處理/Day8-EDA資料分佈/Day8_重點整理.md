# Day7-EDA資料分佈重點整理
## 知識點目標：
1. 了解如何通過基本的統計數值以及畫圖來了解資料

## EDA - 統計量化的方式？
- 計算集中趨勢   
    - 平均值 Mean
    - 中位數 Median
    - 眾數 Mode
- 計算資料分散程度
    - 最小值 Min
    - 最大值 Max
    - 範圍 Range
    - 四分位差 Quartiles
    - 變異數 Variance
    - 標準差 Standard deviation
- 使用統計特徵可以讓我們初步了解資料，並且觀察是否有異常值...等情況
- [EDA 視覺化方式](https://matplotlib.org/3.2.2/gallery/index.html)：Matplotlib

## 知識點複習
1. 資料大部分時候都是非常多的，平均值、標準差、最大最小值等統計數值能幫助我們迅速對資料有初步的了解。
2. 了解統計數值後，把資料的圖畫出來除了能夠更全面地了解資料，也能幫我們快速觀察到異常的地方
3. pandas 有許多已經寫好用來做以上這些觀察的函數，熟悉這些函數的使用能加速觀察資料的過程

## 延伸閱讀
1. [敘述統計與機率分布](http://www.hmwu.idv.tw/web/R_AI_M/AI-M1-hmwu_R_Stat&Prob_v2.pdf)
要做出足夠深入的 EDA，對於統計的理解是必須的。

2. [常見的統計分佈](https://www.healthknowledge.org.uk/public-health-textbook/research-methods/1b-statistical-methods/statistical-distributions)
這個網頁描述了幾個常見的分布：常態分布 / 二項式分布 / 卜瓦松分布，其中常態分布是最常使用到的。