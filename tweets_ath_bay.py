import json
import pandas as pd
import matplotlib.pyplot as plt

tweets_data_path = '/home/rohit/twitter_data_athvsbay.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

#print len(tweets_data)
tweets = pd.DataFrame()
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
#tw = open('tw.txt', 'w')
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

tweets_by_country = tweets['country'].value_counts()

'''fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Countries', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')
plt.show()'''

import re

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

tweets['atletico'] = tweets['text'].apply(lambda tweet: word_in_text('atletico', tweet))
tweets['bayern'] = tweets['text'].apply(lambda tweet: word_in_text('bayern', tweet))

print tweets['atletico'].value_counts()[True]
print tweets['bayern'].value_counts()[True]

teams = ['atletico', 'bayern']
tweets_by_teams = [tweets['atletico'].value_counts()[True], tweets['bayern'].value_counts()[True]]

x_pos = list(range(len(teams)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_teams, width, alpha=1, color='g')

# Setting axis labels and ticks
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: atletico vs bayern(raw data)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(teams)
plt.show()





