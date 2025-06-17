import numpy as np
import pandas as pd

import tensorflow as tf
from tensorflow import keras
from keras import layers

import clean_data
import settings

settings.init()

logs_dir = settings.logs_dir
model_dir = settings.model_dir
files_dir = settings.files_dir

data = pd.read_csv(settings.get_file_path("QS.csv"), encoding="latin1")

#delete & purge the wrong data
data = data[~data["STATUS"].map(lambda x: isinstance(x, float))]
data["RANK_2025"] = data["RANK_2025"].map(clean_data.clean_rank)
data["SIZE"] = data["SIZE"].map(clean_data.clean_size)
data["RES."] = data["RES."].map(clean_data.clean_res)

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
data.to_csv(settings.get_file_path("output/result.csv"))

# 6:2:2
RowCT = data.shape[0]

# random index
indexes = np.random.permutation(RowCT)

TD_index = indexes[:int(RowCT*0.6)]
VD_index = indexes[int(RowCT*0.6):int(RowCT*0.8)]
XD_index = indexes[int(RowCT*0.8):]

# split data
train_data = data.iloc[TD_index]
val_data = data.iloc[VD_index]
test_data = data.iloc[XD_index]

# save data
# train_data.to_csv(settings.get_file_path("output/train.csv"), index=False)
# val_data.to_csv(settings.get_file_path("output/val.csv"), index=False)
# test_data.to_csv(settings.get_file_path("output/test.csv"), index=False)

# normalization
tv_data = pd.concat([train_data, val_data])
mean = tv_data.mean()
std = tv_data.std()

train_data = (train_data - mean) / std
val_data = (val_data - mean) / std
test_data = (test_data - mean) / std

y_train = np.array(train_data["RANK_2025"])
x_train = np.array(train_data.drop(["RANK_2025"], axis="columns"))
y_val = np.array(val_data["RANK_2025"])
x_val = np.array(val_data.drop(["RANK_2025"], axis="columns"))
x_test = np.array(test_data.drop(["RANK_2025"], axis="columns"))
y_test = np.array(test_data["RANK_2025"])

# build model
model = keras.Sequential(name="QS_Rank_Predictor")
model.add(layers.Dense(64, activation='relu', input_shape=(x_train.shape[1],)))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(1))

print(model.summary())

# compile model
model.compile(optimizer=keras.optimizers.Adam(0.001),
              loss=keras.losses.MeanAbsoluteError(),
              metrics=[keras.metrics.MeanAbsoluteError()])

# save model
model_cbk = keras.callbacks.TensorBoard(log_dir = logs_dir)
model_mckpt = keras.callbacks.ModelCheckpoint(settings.get_model_path("QS_Rank_Predictor.h5"),  
                                                  save_best_only=True, 
                                                  monitor='val_mean_absolute_error', 
                                                  mode='min')

# train model
# """
history = model.fit(x_train, y_train,
            validation_data=(x_val, y_val),
            epochs=300,
            batch_size=64,
            callbacks=[model_cbk, model_mckpt],
            )
# """

# print(history.history.keys())

# check accuracy
model.load_weights(settings.get_model_path("QS_Rank_Predictor.h5"))
y_pred = model.predict(x_test)
y_perd = np.reshape(y_pred * std["RANK_2025"] + mean["RANK_2025"], (y_pred.shape[0],))

p_error = np.mean(np.abs(y_test-y_pred)) / np.mean(y_test)
print(f"Prediction Error: {p_error: 5.2%}%")