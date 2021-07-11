# 教學目標：知道 DataFrame 如何檢視欄位的型態數量以及各欄型態, 以及 Label Encoding / One Hot Encoding 如何寫?
# 範例重點：1.檢視 DataFrame 的資料型態 2.了解 Label Encoding 如何寫 3.了解 One Hot Encoding 如何寫
import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# 設定 data_path
dir_data = './data/'
f_app_train = os.path.join(dir_data, 'application_train.csv')
f_app_test = os.path.join(dir_data, 'application_test.csv')
app_train = pd.read_csv(f_app_train)
app_test = pd.read_csv(f_app_test)

# 檢視資料中各個欄位類型的數量 
app_train_count = app_train.dtypes.value_counts()
print(app_train_count)

# 檢視資料中類別型欄位各自類別的數量
app_train_object_count = app_train.select_dtypes(include=["object"]).apply(pd.Series.nunique, axis = 0)
print(app_train_object_count)

# Create a label encoder object
le = LabelEncoder()
le_count = 0

# Iterate through the columns
for col in app_train:
    if app_train[col].dtype == 'object':
        # If 2 or fewer unique categories
        if len(list(app_train[col].unique())) <= 2:
            # Train on the training data
            le.fit(app_train[col])
            # Transform both training and testing data
            app_train[col] = le.transform(app_train[col])
            app_test[col] = le.transform(app_test[col])
            
            # Keep track of how many columns were label encoded
            le_count += 1
            
print('%d columns were label encoded.' % le_count)

# One Hot encoding
app_train = pd.get_dummies(app_train)
app_test = pd.get_dummies(app_test)
print('----one hot encoding----')
print(app_train['CODE_GENDER_F'].head())
print(app_train['CODE_GENDER_M'].head())
print(app_train['NAME_EDUCATION_TYPE_Academic degree'].head())