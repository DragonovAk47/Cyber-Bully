# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 02:56:44 2020

@author: Grindelwald
"""

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
    lem = WordNetLemmatizer()
    tokens = [lem.lemmatize(i,'v') for i in x]
    text = ' '.join(tokens)
    return text

def model(text,bow,dct):
 
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




