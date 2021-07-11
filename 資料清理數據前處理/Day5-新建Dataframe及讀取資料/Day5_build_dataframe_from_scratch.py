# 教學目標：1.Pandas處理最常用的資料格式, 試著使用不同的方式新建一個 DataFrame 2.練習DataFrame對資料的操作
# 範例重點：1.新建DataFrame方法一 2.新建DataFrame方法二 3.資料操作：groupby
import pandas as pd

# 方法一
data = {'weekday': ['Sun', 'Sun', 'Mon', 'Mon'],
        'city': ['Austin', 'Dallas', 'Austin', 'Dallas'],
        'visitor': [139, 237, 326, 456]}
visitors_1 = pd.DataFrame(data)
print(visitors_1)

# 方法二
cities = ['Austin', 'Dallas', 'Austin', 'Dallas']
weekdays = ['Sun', 'Sun', 'Mon', 'Mon']
visitors = [139, 237, 326, 456]

list_labels = ['city', 'weekday', 'visitor']
list_cols = [cities, weekdays, visitors]

zipped = list(zip(list_labels, list_cols))

visitors_2 = pd.DataFrame(dict(zipped))
print(visitors_2)

#計算每個weekday的平均visitor數量，
weekday_mean = visitors_1.groupby(by="weekday")['visitor'].mean()
print(weekday_mean)