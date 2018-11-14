# https://www.kaggle.com/ngyptr/python-nltk-sentiment-analysis/notebook
#http://www.pingshiuanchua.com/blog/post/simple-sentiment-analysis-python?utm_campaign=News&utm_medium=Community&utm_source=DataCamp.com
import nltk
from main import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
# nltk.download('vader_lexicon')

def nltk_sentiment(sentence):
    nltk_sentiment = SentimentIntensityAnalyzer()
    score = nltk_sentiment.polarity_scores(sentence)
    return score

dataset = onlyMessages(getJson('messages/hn.json'))
nltk_results = [nltk_sentiment(row) for row in dataset]
print('one')
results_df = pd.DataFrame(nltk_results)
print('two')
text_df = pd.DataFrame(dataset, columns = ['text'])
print('three')
nltk_df = text_df.join(results_df)
