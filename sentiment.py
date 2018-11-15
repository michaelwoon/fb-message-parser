# https://www.kaggle.com/ngyptr/python-nltk-sentiment-analysis/notebook
#http://www.pingshiuanchua.com/blog/post/simple-sentiment-analysis-python?utm_campaign=News&utm_medium=Community&utm_source=DataCamp.com
import nltk
from main import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import openpyxl
# nltk.download('vader_lexicon')

def sentiment(filename,name):
    nltk_sentiment = SentimentIntensityAnalyzer()
    dataset = onlyMessages(getJson(filename))
    nltk_results = [nltk_sentiment.polarity_scores(row) for row in dataset]
    # {'neg': 0.0, 'neu': 0.238, 'pos': 0.762, 'compound': 0.4939}
    neg = 0
    neu = 0
    pos = 0
    compound = 0
    for item in nltk_results:
        neg += item['neg']
        neu += item['neu']
        pos += item['pos']
        compound += item['compound']
    print(neg)
    print(neu)
    print(pos)
    print(compound)
    results_df = pd.DataFrame(nltk_results)
    text_df = pd.DataFrame(dataset, columns = ['text'])
    nltk_df = text_df.join(results_df)
    writer = pd.ExcelWriter(name + '.xlsx')
    nltk_df.to_excel(writer,sheet_name='Sheet1')
    writer.save()
