import investpy as ip
import datetime
import snscrape.modules.twitter as sntwitter
from datetime import datetime, timedelta

class ScrapeStockTweet:
    
    def __init__(self):
        self.date = datetime.now().date()
    
    def getStock(self, date):
        from_date = date
        to_date = date+1
        # from_date = str(self.date.day) +'/'+ str(self.date.month) +'/'+ str(self.date.year)
        # to_date = str(self.date.day+1) +'/'+ str(self.date.month) +'/'+ str(self.date.year)
        nifty = ip.get_index_historical_data(index='NIFTY 100',country='India', from_date='7/4/2022', to_date='8/4/2022',interval='Daily')
        return nifty.iloc[0]['Close']

    def getTweets(self, date):
        data = {}
        data['date'] = date
        tweets = []
        from_date = date
        to_date = date
        # from_date = datetime.now().strftime('%Y-%m-%d')
        # to_date = (datetime.now() + timedelta(1)).strftime('%Y-%m-%d')
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:NDTVProfit since:'+'2022-04-7'+' until:'+'2022-04-8').get_items()):
            tweets.append(tweet.content)
        data['tweet'] = tweet
        return data
    
    def collectData(self):
        data = {}
        data['date'] = self.date.strftime('%d-%m-%Y')
        data['price'] = self.getStock(0)
        data['tweet'] = self.getTweets(0)
        # print(data['tweets'])
        return data

# ob = ScrapeStockTweet()
# data = ob.collectData()
# print(data)

    