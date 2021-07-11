# 作業目標：試著讀取網頁上的圖片連結清單, 再以清單中網址讀取圖片
# 作業重點：1.從網頁上讀取連結清單 2.從清單網址讀取圖片
import requests
import pandas as pd
from PIL import Image
from io import BytesIO
import numpy as np
import matplotlib.pyplot as plt

# 讀取題目中給予的 txt 檔案
target_url = 'https://raw.githubusercontent.com/vashineyu/slides_and_others/master/tutorial/examples/imagenet_urls_examples.txt'
response = requests.get(target_url)
data = response.text
print(len(data))
print(data[0:100])

# 找到換行符號做字串分割後
data = data.split("\n")
print(len(data))
print(data[0])

# 將 txt 轉成 pandas dataframe¶
arrange_data = []
for i in data:
    l = i.split("\n")
    arrange_data.append(l)
df = pd.DataFrame(arrange_data)
print(df.head())

# 讀取前 5 張圖片
response = requests.get(df.iloc[[0],[0]])
print(response)
image = Image.open(BytesIO(response.content))
image = np.array(image)
print(image.shape)
plt.imshow(image)
plt.show()


def img2arr_fromURLs(url_list, resize = False):
    img_list = []
    for i in url_list:
        response = requests.get(i)
        img = Image.open(BytesIO(response.content))
        if resize:
                img = img.resize((256,256))
            #img = np.array(img)
            #img_list.append(img)
    
    return img_list

result = img2arr_fromURLs(df[0:5][1].values)
print("Total images that we got: %i " % len(result)) 

for im_get in result:
    plt.imshow(im_get)
    plt.show()
