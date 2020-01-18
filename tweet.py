import tweepy
import threading ,time
import re
import pandas as pd
import nltk

from nltk.corpus import stopwords
import requests
def nudity(url):
    r = requests.post(
        "https://api.deepai.org/api/nsfw-detector",
        data={
            'image': url,
        },
        headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
    )
    print(r.json())

import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from nltk import WordNetLemmatizer
bow = pickle.load(open("tfidf.pickle",'rb'))
dct = pickle.load(open("finalized_model1.sav",'rb'))
# -*- coding: utf-8 -*-
badwords = []
for line in open("badwords.txt"):
    for word in line.split( ):
        badwords.append(word)

def remove_user_handle(text):
    pattern = "@[\w]*"
    r=  re.findall(pattern,text)
    
    for i in r:
        text = re.sub(i,"",text)
    return text

def remove_stopwords(text):
    text = ' '.join([w for w in text.split() if w.lower() not in stopwords.words('english')])
    text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())
    return text

def lemmatize(text):
    x = text.split()
    for word in x:
        if word in badwords:
            print(word)
            return 1
   

def model(text,bow,dct):
    if lemmatize(text[0]):
        return 1
    
    bow_matrix = bow.transform(text)
    df_bow = pd.DataFrame(bow_matrix.todense())
    y_pred  =dct.predict(df_bow)
    return y_pred

def main(text,bow,dct):
    
    text = remove_user_handle(text)
    text = remove_stopwords(text)
    text = [text]
    pred = model(text,bow,dct)
    return pred





consumer_key = 'FtdxPkwxNycQsoff0YyBT6mhr'
consumer_secret = 'Y7xcl4yvOzHCbUG1lQo6KcuX9CocVFwaO8pEp2QCI70Yh1jxuS'

access_token = '808233723481100288-DreiznXUXvFUJ25CUkbe3pcmixsa4ia'
access_token_secret = 'rD9qXxwt51rdUqgX8FbSCHgGJCMAt3THevNxYpKJd6j9G'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user_id = 'realDonaldTrump'
count=200

result = tweepy.Cursor(api.search, q="@DragonovAK47",tweet_mode='extended').items(1)
       
user_list = ["@realDonaldTrump"]

def tweets(q,count):
    for user in user_list:
        for tweet in tweepy.Cursor(api.search, q=user,tweet_mode='extended').items(count):
            
            print("----------------------------------------------------------------------------")
            if hasattr(tweet, 'retweeted_status'):
                print(tweet.retweeted_status.full_text)
                msg = main(tweet.retweeted_status.full_text,bow,dct)
                if 'media' in tweet.entities:
                      for image in  tweet.entities['media']:
                          print(image['media_url'])
                else:
                      print("no image//////////////")
                          
                print(msg)
                
            else:
                msg = main(tweet.full_text,bow,dct)
                print(tweet.full_text)
                print(msg)

tweets(user_list,4)
    


            
