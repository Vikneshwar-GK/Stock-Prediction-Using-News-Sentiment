import streamlit as st
import pandas as pd
import numpy as np
import pandas_datareader as pdd
import matplotlib.pyplot as plt
import pickle
from datetime import datetime
from keras.models import Sequential, load_model
# from classes.model_prediction import ModelPrediction
import os

def scale(price, score):
    with open(os.path.join(os.getcwd(),'objects/price_scaler.pkl'), 'rb') as inp:
            scale_price = pickle.load(inp)
    with open(os.path.join(os.getcwd(),'objects/score_scaler.pkl'), 'rb') as inp:
            scale_score = pickle.load(inp)

    price = scale_price.fit_transform(price.values.reshape(-1, 1))
    score = scale_score.fit_transform(score.values.reshape(-1, 1))
    return price, score
    
    
    price = scale_price.fit_transform(price.values.reshape(-1, 1))
    score = scale_score.fit_transform(score.values.reshape(-1, 1))
    return np.array(price), np.array(score)

def descale(price):
    with open(os.path.join(os.getcwd(),'objects/price_scaler.pkl'), 'rb') as inp:
            scale_price = pickle.load(inp)
    price = scale_price.inverse_transform(price)
    return price

def createdataset(dataset, scoreset, look_back=1):
	dataX, dataY = [], []
	for i in range(len(dataset)-look_back-1):
		a = dataset[i:(i+look_back)]
		b = scoreset[i:(i+look_back)]
		dataX.append(np.concatenate((a, b), axis=1))
		dataY.append(dataset[i + look_back, 0])
	return np.array(dataX)


# print('bolldd')
st.title('Stock Prediction with News Sentiment')
st.header('Nifty 100 Stock')

general_stock = pdd.DataReader('NSE', 'yahoo', '2016-01-01', '2022-04-10')

st.subheader('Stock Description')
st.write(general_stock.describe())

st.subheader('Last 20 Stock')
st.write(general_stock.tail(20))

dataframe = pd.read_csv(os.path.join(os.getcwd(),'data/StockTweetDataset.csv'))

st.subheader('Closing Price vs Time Chart')
fig = plt.figure(figsize=(12, 6))
plt.plot(dataframe.price)
st.pyplot(fig)

st.subheader('Closing Price vs Time Chart with 100MA')
ma100 = dataframe.price.rolling(100).mean()
fig = plt.figure(figsize=(12, 6))
plt.plot(ma100)
plt.plot(dataframe.price)
st.pyplot(fig)

st.subheader('Closing Price vs Time Chart with 200MA')
ma200 = dataframe.price.rolling(200).mean()
fig = plt.figure(figsize=(12, 6))
plt.plot(ma200)
plt.plot(dataframe.price)
st.pyplot(fig)


price, score = scale(dataframe['price'], dataframe['score'])
to_predict = createdataset(price, score, 60)

model = load_model(os.path.join(os.getcwd(),'model/model.h5'))
prediction = model.predict(to_predict)
prediction = descale(prediction)

st.subheader('Closing Price vs Time Chart')
fig = plt.figure(figsize=(12, 6))
plt.plot(dataframe.price)
plt.plot(prediction)
st.pyplot(fig)
