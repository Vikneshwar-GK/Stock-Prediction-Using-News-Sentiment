import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from tqdm import tqdm
from scrape import ScrapeStockTweet
from data_cleaning import TextCleaning

class SentimentAnalysis:
    def __init__(self):
        self.word_score = {'falls': -9, 'drops': -9, 'rise': 9, 'increases': 9, 'gain': 9, 'hiked': -9, 'dips': -9, 'declines': -9, 'decline': -9, 'hikes': -9, 'jumps': 9,
              'lose': -9, 'profit': 9, 'loss': -9, 'shreds': -9, 'sell': -9, 'buy': 9, 'recession': -9, 'rupee weakens': -9, 'record low': -9, 'record high': 9,
              'sensex up': 9, 'nifty down': -9, 'sensex down': -9, 'nifty up': 9}
    
    def analysis(self, data):
        analyser = SentimentIntensityAnalyzer()
        analyser.lexicon.update(self.word_score)
        data['score'] = analyser.polarity_scores(data['tweet'])['compound']
        return data

# ob = ScrapeStockTweet()
# data = ob.collectData()
# ob1 = TextCleaning()
# data = ob1.cleanData(data)
# ob3 = SentimentAnalysis()
# data = ob3.analysis(data)

# print(data)


