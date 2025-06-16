import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import tensorflow as tf
#from tensorflow import keras
#from tensorflow.keras import layers

data = pd.read_csv("QS.csv", encoding="latin1")

#delete the wrong data
data = data[~data["STATUS"].map(lambda x: isinstance(x, float))]

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


data.to_csv('E.csv')
