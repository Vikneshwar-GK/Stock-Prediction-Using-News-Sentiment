import pandas as pd
import os

class ReadWrite:
    def __init__(self):
        self.dataframe =  pd.read_csv(os.path.join(os.getcwd(),'data/StockTweetDataset.csv'))

    def write(self, data):
        print('write')
    
    def read(self, data):
        print('read')