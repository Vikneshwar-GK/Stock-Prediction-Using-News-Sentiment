from os import scandir
import pandas as pd
import re
from tqdm import tqdm
from scrape import ScrapeStockTweet

class TextCleaning:
    def __init__(self):
        self.tweet = ""

    def decontracted(self, phrase):
        # specific
        phrase = re.sub(r"won't", "will not", phrase)
        phrase = re.sub(r"can\'t", "can not", phrase)

        # general
        phrase = re.sub(r"n\'t", " not", phrase)
        phrase = re.sub(r"\'re", " are", phrase)
        phrase = re.sub(r"\'s", " is", phrase)
        phrase = re.sub(r"\'d", " would", phrase)
        phrase = re.sub(r"\'ll", " will", phrase)
        phrase = re.sub(r"\'t", " not", phrase)
        phrase = re.sub(r"\'ve", " have", phrase)
        phrase = re.sub(r"\'m", " am", phrase)
        return phrase
    
    def clean(self, text):
        text = str(text)
        text = text.lower()
        text = re.sub(r'http\S+', ' ', text)
        text = re.sub(r'pic.twitter\S+', ' ', text)
        text = self.decontracted(text)
        text = re.sub(r'\(([^)]+)\)', " ", text)
        text = text.replace('etmarkets', ' ').replace('marketupdates', ' ').replace('newsalert', ' ').replace('ndtv', ' ').replace('moneycontrol', ' ').replace('here is why', ' ')
        text = text.replace('marketsupdate', ' ').replace('biznews', ' ').replace('click here', ' ').replace('live updates', ' ').replace('et now', ' ')
        text = re.sub(r'[^a-zA-Z ]+', ' ', text)
        text = re.sub(r' \w{1,2}_', ' ', text)
        text = re.sub('\s+',' ', text)
        return text

    def removeSingleChar(self, text):
        processed_text = ""
        for i in text.split():
            if len(i)>2:
                processed_text += i + " "
        return processed_text.strip()
    
    def cleanData(self, data):
        for i in range(len(data['tweet'])):
            data['tweet'][i] = self.clean(data['tweet'][i])
            data['tweet'][i] = self.removeSingleChar(data['tweet'][i])
        data['tweet'] = ' '.join([str(elem) for elem in data['tweet']])
        return data

# ob = ScrapeStockTweet()
# data = ob.collectData()
# ob1 = TextCleaning()
# data = ob1.cleanData(data)
# print(data)
