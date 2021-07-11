# Day1-資料介紹與評估指標重點整理
## 知識點目標
1. 準備進入資料科學領域的概念流程與關鍵

### 學習路徑
- 找到問題：挑一個有趣的問題，並從解決一個簡單的問題開始
- 初探：在這個題目上做一個原型解決方案
- 改進：試圖改進原型解決方案並從中學習(如代碼優化、速度優化、演算法優化)
- 分享：試著記錄並分享解決方案歷程
- 練習：不斷於不同問題上反覆練習
- 實戰：認真參與一場比賽

### 一開始接觸到大量資料時, 可以思考哪些問題
- 透過資料研究的議題有何重要性？
    - 企業的核心問題，如：用戶廣告投放
    - 對世界有貢獻，如：肺癌預測
- 資料從何而來？
    - 資料來源與資料品質息息相關
    - 不同資料源可以推測其資料異常的理由及可能性
- 資料的型態為何？
    - 結構化資料：需檢視欄位意義及名稱，資料類型如：數值、表格
    - 非結構化資料：需思考資料轉換與標準化方式，資料類型如：圖片、影音
- 我們可以從資料中回答什麼問題(指標)？
    - 每個問題都應該要可以被驗證，有一個可供衡量的數學評估指標
    - 常見的衡量指標如下
        - 分類問題：正確率、AUC、MAP、損失函數 - Binary Cross Entropy (CE)...等
        - 迴歸問題：MAE、RMSE...等
   
### 補充資料：機器學習中的Evaluation Metrics
1. (Confusion Matrix) 把True Positive和True Negative加總除上所有情形個數就是Accuracy
2. 若只使用Accuracy作為判斷標準可能會失效，也就是Accuracy Paradox現象，因此增加Precision(準確率)和Recall(召回率)兩個判斷指標來更明確的表達內容
3. Precision看的是在預測正向的情形下，實際的「精準度」是多少，而Recall則是看在實際情形為正向的狀況下，預測「能召回多少」實際正向的答案
4. F1 Score 或 F1 Measure代表Precision和Recall同等重要

### 參考資料：
1. https://blog.csdn.net/aws3217150/article/details/50479457
2. https://www.ycc.idv.tw/confusion-matrix.html

### 補充資料二：損失函數

### 參考資料：
1. https://towardsdatascience.com/understanding-binary-cross-entropy-log-loss-a-visual-explanation-a3ac6025181a

## 知識點複習
1. 初入資料科學的探索流程
2. 找到問題 → 初探 → 改進 → 分享 → 練習 → 實戰
3. 面對問題需要思考的關鍵點

## 延伸閱讀
無