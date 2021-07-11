# Day16-EDA:不同數值範圍間的特徵如何檢視/繪圖與樣式Kernel Density Estimation (KDE)重點整理
## 知識點目標
1. 知道 matplotlib 的其他 theme
2. 學會什麼是 Kernel Density Estimation (KDE) 與如何繪製

### 繪圖風格
- plt.style.use(‘default’) # 不需設定就會使用預設
- plt.style.use('ggplot')
- plt.style.use(‘seaborn’) # 採用 seaborn 套件繪圖

### Kernel Density Estimation (KDE)
- 採用無母數方法畫出一個觀察變數的機率密度函數
    - 某個 X 出現的機率為何
- Density plot 的特性
    - 歸一：線下面積和為 1
    - 對稱：K(-u) = K(u)
- 常用的 Kernel function
    - Gaussian (Normal dist)
    - Cosine

## 知識點複習
1. KDE 的優點與缺點
    - 優：無母數方法，對分布沒有假設 (使用上不需擔心是否有一些常見的特定假設，如分布為常態)
    - 缺：計算量大，電腦不好可能跑不動
2. 透過 KDE plot，我們可以較為清楚的看到不同組間的分布差異

## 延伸閱讀
1. [Python Graph Gallery](https://www.python-graph-gallery.com/)
