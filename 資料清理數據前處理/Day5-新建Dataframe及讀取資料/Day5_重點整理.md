# Day5-如何新建一個 dataframe?如何讀取其他資料?(非 csv 的資料)重點整理
## 知識點目標：
1. 了解如何快速驗證 dataframe 操作的程式碼
2. 學會如何讀取其他資料格式：txt / jpg / png / json / mat / npy / pkl ...

### 為什麼新建一個 dataframe 重要？
- 需要把分析過程中所產生的數據或者結果儲存為結構化的資料
- 測試程式碼
    - 若原始資料太大，操作相對費時，可以先在具有同樣結構的資料上測試程式碼是否能夠得到理想中的結果。
    - 不確定視覺化程式碼中所需要的資料結構，用新建立的 dataframe 結構來去了解，而不是急著在原始資料上操作。

### 讀取其他非csv資料格式？

檔案格式

- 圖像檔 (PNG / JPG …)
讀取範例：
```
import cv2
image = cv2.imread(...) # 注意 cv2 會以 BGR 讀入
image = cv2.cvtcolor(image, cv2.COLOR_BGR2RGB)

from PIL import Image
image = Image.read(...)
import skimage.io as skio
image = skio.imread(...)
```

- Python npy
讀取範例：
```
import numpy as np
arr = np.load(example.npy)
```

- Pickle (pkl)
讀取範例：
```
import pickle
with open(‘example.pkl’, ‘rb’) as f:
arr = pickle.load(f)
```

## 知識點複習
1. 資料量很大時，可以先在具有同樣結構的小樣本驗證程式碼執行的結果是否符合預期
2. 用 pd.DataFrame 來創建一個 dataframe
3. 用 np.random.randint 來產生隨機數值
4. 不同的資料有不同讀取方式
    - 文字格式：通常可以用 with open()
    - 圖像格式：可以使用 PIL, Skimage 或是 CV2 (CV2 的速度較快，但須注意讀入的格式為 BGR)
    - 其他形式如 npy / pickle 可以儲存經過處理後的資料

### 延伸閱讀
1. [Pandas Foundations](https://www.datacamp.com/courses/pandas-foundations)
    - 閱讀後重點整理：

2. [Github repo](https://github.com/guipsamora/pandas_exercises)