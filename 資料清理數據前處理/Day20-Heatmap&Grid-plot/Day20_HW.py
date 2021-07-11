# 作業目標：設定隨機資料, 並依照範例練習基礎與進階的 Heatmap
# 作業重點：1.條件隨機矩陣, 並仿造基礎 Heatmap 範例作圖 2.條件隨機數值列, 並仿造進階 Heatmap 範例作圖
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
plt.style.use('ggplot')

matrix = (np.random.random((10, 10)) - 0.5) * 2
plt.figure(figsize=(10,10))
heatmap = sns.heatmap(matrix, cmap = plt.cm.RdYlBu_r, vmin = -1., vmax = 1., annot = True)
plt.show()

nrow = 1000
ncol = 3
matrix = (np.random.random((1000, 3)) - 0.5)*2

# 隨機給予 0, 1, 2 三種標籤
indice = np.random.choice([0,1,2], size=nrow)
plot_data = pd.DataFrame(matrix, indice).reset_index()

# 繪製 seborn 進階 Heatmap
grid = sns.PairGrid(data = plot_data, size = 3, diag_sharey=False, hue = 'index', vars = [x for x in list(plot_data.columns) if x != 'index'])
grid.map_upper(plt.scatter , alpha = 0.2)
grid.map_diag(sns.kdeplot)
grid.map_lower(sns.kdeplot, cmap = plt.cm.OrRd_r)
plt.show()

nrow = 1000
ncol = 3
matrix = np.random.randn(nrow * ncol).reshape((nrow, ncol))

# 隨機給予 0, 1, 2 三種標籤
indice = np.random.choice([0, 1, 2], size = nrow)
plot_data = pd.DataFrame(matrix, indice).reset_index()

# 繪製 seborn 進階 Heatmap
grid = sns.PairGrid(data = plot_data, size = 3, diag_sharey=False, hue = 'index', vars = [x for x in list(plot_data.columns) if x != 'index'])
grid.map_upper(plt.scatter , alpha = 0.2)
grid.map_diag(sns.kdeplot)
grid.map_lower(sns.kdeplot, cmap = plt.cm.OrRd_r)
plt.show()