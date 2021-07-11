# Day19-Subplots重點整理
## 知識點目標
1. 學會如何使用 subplots

### Subplot - 讓圖可以適度地呈現
- 什麼時候該使用 subplot?
    - 有很多相似的資訊要呈現時 (如不同組別的比較)
    - 同一組資料，但想同時用不同圖型呈現時

## 知識點複習
1. 適度地將圖片分格呈現，有助於資訊傳達
2. 但過度使用 subplots 也將會使得資訊太多反而讓重點混淆
3. Subplot 的坐標系 (列-欄-位置)

## 延伸閱讀
1. [Subplot](https://matplotlib.org/2.0.2/examples/pylab_examples/subplots_demo.html)
- matplotlib 官方介紹 subplot 的排版範例，裡面有縱向並列，橫向並列等各式排版，還附上對應的語法

2. [複雜版 subplot 寫法](https://jakevdp.github.io/PythonDataScienceHandbook/04.08-multiple-subplots.html)

3. [另類子圖 Seaborn.jointplot](https://seaborn.pydata.org/generated/seaborn.jointplot.html)
- 除了圖本身的排版，搭配排版的圖組，有時也是不錯的選擇
- 最經典的 Seaborn.jointplot，除了繪製兩個變數間的散佈圖外，變數本身的分布長條圖，也會列在對應的軸上，讓人一目了然，中央的散佈圖也有點狀 / 等高線 / 蜂巢等不同選擇
- EDA的重點是讓人看懂資料，因此圖形是否直覺是相當重要的一環