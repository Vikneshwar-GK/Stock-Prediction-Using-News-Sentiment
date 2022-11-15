import pandas as pd
import os
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from data_cleaning import TextCleaning
from scrape import ScrapeStockTweet
from sentiment_analysis import SentimentAnalysis


class DataPreprocessing:

    def __init__(self, data):
        self.scale_price = MinMaxScaler() #read pkl file
        self.scale_score = MinMaxScaler() #read pkl file
        self.dataframe = pd.read_csv(os.path.join(os.getcwd(),'data/StockTweetDataset.csv'))
        data['sentiment'] = 0
        # self.dataframe = self.dataframe.append(data, ignore_index=True)

    def scaler(self):
        date = self.dataframe['date'][-60:]
        price = self.dataframe['price'][-60:]
        score = self.dataframe['score'][-60:]
        
        price = self.scale_price.fit_transform(price.values.reshape(-1, 1))
        score = self.scale_score.fit_transform(score.values.reshape(-1, 1))
        
        data = {}
        data['date'] = date
        data['price'] = price
        data['score'] = score
        data['predict'] = np.concatenate((data['price'], data['score']), axis=1)
        data['predict'] = data['predict'][np.newaxis,:,:]
        # data['predict'] = [data['predict']]
        # shape = data['predict'].shape
        # data['predict'] = np.array(data['predict'])
        # np.reshape(data['predict'], (1, shape[0], shape[1]))
        # print(data['predict'])
        print(data['predict'].shape)
        
        return data

# ob = ScrapeStockTweet()
# data = ob.collectData()
# ob1 = TextCleaning()
# data = ob1.cleanData(data)
# ob3 = SentimentAnalysis()
# data = ob3.analysis(data)

# ob = DataPreprocessing(data)
# ob.scaler()
