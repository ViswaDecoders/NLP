import os
from os import path
from PIL import Image
from flashtext import KeywordProcessor
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv(r"book1.csv",encoding ="latin-1",dtype='object')

df.dropna()
df.dropna(axis='columns')
comment_words = ''
stopwords = set(STOPWORDS)
stopwords.add('')

currdir = os.path.dirname(__file__)

for val in df.review_body:
    val = str(val);
    tokens = val.split()
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()

    comment_words+=" ".join(tokens)+" "

p = KeywordProcessor(case_sensitive = False)
p.add_keyword('nan nan',' ');
p.add_keyword('is','company');
comment_words = p.replace_keywords(comment_words)

mask = np.array(Image.open(os.path.join(currdir,'upvote.png')))
wordcloud = WordCloud(width = 3000, height = 2000,mask=mask,
                      background_color = 'white', 
                      stopwords =STOPWORDS).generate(comment_words)

text_dictionary = wordcloud.process_text(comment_words)
word_freq={k: v for k,v in sorted(text_dictionary.items(),reverse=True, key=lambda item:item[1])}

rel_freq=wordcloud.words_
print("List of words frequently repeated: \n")
print('{:<10}{:<10}'.format('Words','frequency'))
for key,value in list(word_freq.items())[:10]:
    print('{:<10}{:<10}'.format(key,value))

print("\nList of words frequently repeated(ratios): \n")

print('{:<10}{:<10}'.format('Words','ratio frequency'))
for key,value in list(rel_freq.items())[:10]:
    print('{:<10}{:<10}'.format(key,value))

plt.figure(figsize = (8,8), facecolor = None)
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad=0)


from nltk.sentiment.vader import SentimentIntensityAnalyzer

message_text = a = '.'.join(df.review_body.tolist())

sid=SentimentIntensityAnalyzer()
scores = sid.polarity_scores(message_text[:1000000])
print('\npie chart Sentiment scores\n')
for key in sorted(scores):
    print('{0}: {1}\n, '.format(key,scores[key]), end='')

labels = ['negative','neutral','positive']
sizes = [scores['neg'],scores['neu'],scores['pos']]

plt.figure(2)
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.show()
