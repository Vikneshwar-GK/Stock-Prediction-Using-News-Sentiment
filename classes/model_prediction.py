from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential, load_model
import os
from data_preprocessing import DataPreprocessing
from data_cleaning import TextCleaning
import pickle
from scrape import ScrapeStockTweet
from sentiment_analysis import SentimentAnalysis


class ModelPrediction:
    def __init__(self):
        with open(os.path.join(os.getcwd(),'objects/price_scaler.pkl'), 'rb') as inp:
            self.scale_price = pickle.load(inp)
        # self.dataframe = pd.read_csv(os.path.join(os.getcwd(),'data/StockTweetDataset.csv'))
        self.model = load_model(os.path.join(os.getcwd(),'model/model.h5'))

    def predictStock(self, data):
        predicted_value = self.model.predict(data['predict'])
        predicted_value = self.scale_price.inverse_transform(predicted_value)


        
# ob = ScrapeStockTweet()
# data = ob.collectData()
# ob1 = TextCleaning()
# data = ob1.cleanData(data)
# ob3 = SentimentAnalysis()
# data = ob3.analysis(data)

# ob = DataPreprocessing(data)
# data = ob.scaler()

# ob = ModelPrediction()
# # print(data)
# ob.predictStock(data)
        
