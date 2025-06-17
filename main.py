import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

#import tensorflow as tf
#from tensorflow import keras
#from tensorflow.keras import layers

from clean_rank import clean_rank

data = pd.read_csv("files/QS.csv", encoding="latin1")

#delete & purge the wrong data
data = data[~data["STATUS"].map(lambda x: isinstance(x, float))]
data["RANK_2025"] = data["RANK_2025"].map(clean_rank)

#delete col we don't need
data.drop(["RANK_2024"], axis="columns", inplace=True)
data.drop(["Institution_Name"], axis="columns", inplace=True)
data.drop(["Location"], axis="columns", inplace=True)
data.drop(["Region"], axis="columns", inplace=True)
data.drop(["FOCUS"], axis="columns", inplace=True)
data.drop(["STATUS"], axis="columns", inplace=True)
data.drop(["Overall_Score"], axis="columns", inplace=True)

data.drop(["Academic_Reputation_Rank"], axis="columns", inplace=True)
data.drop(["Employer_Reputation_Rank"], axis="columns", inplace=True)
data.drop(["Faculty_Student_Rank"], axis="columns", inplace=True)
data.drop(["Citations_per_Faculty_Rank"], axis="columns", inplace=True)
data.drop(["International_Faculty_Rank"], axis="columns", inplace=True)
data.drop(["International_Students_Rank"], axis="columns", inplace=True)
data.drop(["International_Research_Network_Rank"], axis="columns", inplace=True)
data.drop(["Employment_Outcomes_Rank"], axis="columns", inplace=True)
data.drop(["Sustainability_Rank"], axis="columns", inplace=True)

# test
#data.to_csv('files/output/result.csv')

# 6:2:2
x = data.drop(["RANK_2025"], axis=1) 
y = data["RANK_2025"]

# 第一次分割
x_train_val, x_test, y_train_val, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#第二次分割
x_train, x_val, y_train, y_val = train_test_split(x_train_val, y_train_val, test_size=0.25, random_state=42)

#檢查比例
print(f"訓練資料: {len(x_train)} 筆 ({len(x_train)/len(x)*100:.1f}%)")
print(f"驗證資料: {len(x_val)} 筆 ({len(x_val)/len(x)*100:.1f}%)")
print(f"測試資料: {len(x_test)} 筆 ({len(x_test)/len(x)*100:.1f}%)")

#儲存資料
x_train.to_csv('files/output/train_features.csv', index=False)
y_train.to_csv('files/output/train_target.csv', index=False)
x_val.to_csv('files/output/val_features.csv', index=False)
y_val.to_csv('files/output/val_target.csv', index=False)
x_test.to_csv('files/output/test_features.csv', index=False)
y_test.to_csv('files/output/test_target.csv', index=False)
