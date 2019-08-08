from keras.layers import Input, Dense, Dropout
from keras.models import Model
from keras import backend as K
import tensorflow as tf
import pandas as pd
import numpy as np

compare_data = pd.read_csv('compare2.csv')
x = compare_data[['Count','Index']]
y =  compare_data['Search']
x_data = np.array(x)
y_data = np.array(y)
y_data = y_data.reshape(-1, 1)
y_data = y_data/100
x_data = x_data/100
x_data
y_data

BATCH_SIZE = 128
NUM_EPOCHS = 20


K.clear_session()

input_layer = Input(batch_shape=(None,x_data.shape[1]))
first_layer = Dense(2, activation='relu', name = "first")(input_layer)
#first_dropout = Dropout(0.5, name="firstdout")(first_layer)

#second_layer = Dense(128, activation='relu', name = "second")(first_layer)
#second_dropout = Dropout(0.5, name="seconddout")(second_layer)

output_layer = Dense(y_data.shape[1], activation='relu', name = "output")(first_layer)

predict_search = Model(input_layer, output_layer)
predict_search.compile(optimizer = "adam", loss="mse", metrics=["accuracy"])
predict_search.fit(x_data, y_data, batch_size=349, epochs=NUM_EPOCHS, verbose=1, validation_split = 0.2)