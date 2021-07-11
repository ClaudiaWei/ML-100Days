### 作業目標：持續接觸有關機器學習的相關專案與最新技術
### 作業重點：透過觀察頂尖公司的機器學習文章，來了解各公司是怎麼應用機器學習在實際的專案上

### 作業內容：以下網站都會整理最新的機器學習專案或者是技術文章，請挑選一篇文章閱讀並試著回答

專案的目標？ (要解決什麼問題）
使用的技術是？ (只需知道名稱即可，例如：使用 CNN 卷積神經網路做影像分類)
資料來源？
- Google AI blog (https://ai.googleblog.com/)
- Facebook Research blog (https://research.fb.com/blog/)
- Apple machine learning journal (https://machinelearning.apple.com/)
- 機器之心 (https://www.jiqizhixin.com/)
- 雷鋒網 (https://www.leiphone.com/category/ai)

### 作業文章重點整理

挑選文章為 [Google AI Blog - 3D Scene Understanding with TensorFlow 3D](https://ai.googleblog.com/2021/02/3d-scene-understanding-with-tensorflow.html)

- 此篇文章主要描述機器學習在3D領域的應用，Google AI推出TensorFlow 3D(TF 3D)
- 文中提及TF 3D使研究團隊能夠開發、訓練、部署最先進的3D模型
>  TF 3D provides a set of popular operations, loss functions, data processing tools, models and metrics that enables the broader research community to develop, train and deploy state-of-the-art 3D scene understanding models.
- TF 3D 包含最先進的3D語意分割、3D物件偵測和3D實體分割的訓練和評估任務，也支援分散式訓練。
> TF 3D contains training and evaluation pipelines for state-of-the-art 3D semantic segmentation, 3D object detection and 3D instance segmentation, with support for distributed training.
- 目前支援Waymo Open、 ScanNet和Rio數據集
> It currently supports the Waymo Open, ScanNet, and Rio datasets.
- 3D Semantic Segmentation
> The 3D semantic segmentation model has only one output head for predicting the per-voxel semantic scores, which are mapped back to points to predict a semantic label per point.
- 3D Instance Segmentation
> The 3D instance segmentation algorithm used in TF 3D is based on our previous work on 2D image segmentation using deep metric learning. 
- 3D Object Detection
> The 3D object detection model predicts per-voxel size, center, and rotation matrices and the object semantic scores.
