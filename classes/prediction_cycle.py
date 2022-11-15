from multiprocessing.dummy import active_children
from typing_extensions import Self
import pandas as pd
import os
import pickle
from scrape import ScrapeStockTweet
from datetime import datetime
from data_cleaning import TextCleaning
from sentiment_analysis import SentimentAnalysis

class PredictionCycle:
    
    def __init__(self):
        self.dataframe = pd.read_csv(os.path.join(os.getcwd(),'data/StockTweetDataset.csv'))

        with open(os.path.join(os.getcwd(),'objects/price_scaler.pkl'), 'rb') as inp:
            self.scale_price = pickle.load(inp)
        
        with open(os.path.join(os.getcwd(),'objects/score_scaler.pkl'), 'rb') as inp:
            self.scale_score = pickle.load(inp)
        
        self.scrape = ScrapeStockTweet()
        self.date = datetime.now()
        
        # if(self.date.weekday<5):
        #     self.isWeekend = False
        # else:
        #     self.isWeekend = True
    
    def evaluation(self):
        
        if(self.date.weekday-1 < 5):
            prevDayWeekDay = True
        else:
            prevDayWeekDay = False
        
        if(prevDayWeekDay):
            # get previous day stock
            actualStock = self.scrape.getStock(self.date)
            # retrain the model
            self.dataframe.iloc[-1]['actual_stock'] = actualStock
            # save the dataframe

    def prediction(self):
        if(self.date.weekday < 5):
            isWeekDay = True
        else:
            isWeekDay = False

        if(isWeekDay):
            # get previous day tweets
            data = ScrapeStockTweet().getTweets(self.date)
            data = TextCleaning().clean(data)
            data = SentimentAnalysis().analysis(data)
            data['sentiment'] = 0
            self.dataframe.append(data)
            



        

    