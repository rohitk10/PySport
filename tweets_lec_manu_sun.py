import json
import pandas as pd
import matplotlib.pyplot as plt

tweets_data_path = 'twitter_sun.txt'

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


import re

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

tweets['manutd'] = tweets['text'].apply(lambda tweet:
                                          (word_in_text('manu', tweet) and word_in_text('win', tweet)) or
                                          (word_in_text('manu', tweet) and word_in_text('vamos', tweet)) or
                                          (word_in_text('manu', tweet) and word_in_text('bueno', tweet)) or
                                          (word_in_text('manu', tweet) and word_in_text('hala', tweet)) or
                                          (word_in_text('manu', tweet) and word_in_text('caray', tweet))or
                                          (word_in_text('manu', tweet) and word_in_text('gewinnen', tweet))or
                                          (word_in_text('manu', tweet) and word_in_text('sieg', tweet))or
                                          (word_in_text('manu', tweet) and word_in_text('komm schon', tweet))or
                                        
                                          (word_in_text('manutd', tweet) and word_in_text('win', tweet)) or
                                          (word_in_text('manutd', tweet) and word_in_text('vamos', tweet)) or
                                          (word_in_text('manutd', tweet) and word_in_text('bueno', tweet)) or
                                          (word_in_text('manutd', tweet) and word_in_text('hala', tweet)) or
                                          (word_in_text('manutd', tweet) and word_in_text('caray', tweet))or
                                          (word_in_text('manutd', tweet) and word_in_text('gewinnen', tweet))or
                                          (word_in_text('manutd', tweet) and word_in_text('sieg', tweet))or
                                          (word_in_text('manutd', tweet) and word_in_text('komm schon', tweet))or

                                          (word_in_text('red devils', tweet) and word_in_text('win', tweet)) or
                                          (word_in_text('red devils', tweet) and word_in_text('vamos', tweet)) or
                                          (word_in_text('red devils', tweet) and word_in_text('bueno', tweet)) or
                                          (word_in_text('red devils', tweet) and word_in_text('hala', tweet)) or
                                          (word_in_text('red devils', tweet) and word_in_text('caray', tweet))or
                                          (word_in_text('red devils', tweet) and word_in_text('gewinnen', tweet))or
                                          (word_in_text('red devils', tweet) and word_in_text('sieg', tweet))or
                                          (word_in_text('red devils', tweet) and word_in_text('komm schon', tweet))or

                                          (word_in_text('manchester', tweet) and word_in_text('win', tweet)) or
                                          (word_in_text('manchester', tweet) and word_in_text('vamos', tweet)) or
                                          (word_in_text('manchester', tweet) and word_in_text('bueno', tweet)) or
                                          (word_in_text('manchester', tweet) and word_in_text('hala', tweet)) or
                                          (word_in_text('manchester', tweet) and word_in_text('caray', tweet))or
                                          (word_in_text('manchester', tweet) and word_in_text('gewinnen', tweet))or
                                          (word_in_text('manchester', tweet) and word_in_text('sieg', tweet))or
                                          (word_in_text('manchester', tweet) and word_in_text('komm schon', tweet))or
 
                                          (word_in_text('devils', tweet) and word_in_text('win', tweet)) or
                                          (word_in_text('devils', tweet) and word_in_text('vamos', tweet)) or
                                          (word_in_text('devils', tweet) and word_in_text('bueno', tweet)) or
                                          (word_in_text('devils', tweet) and word_in_text('hala', tweet)) or
                                          (word_in_text('devils', tweet) and word_in_text('caray', tweet))or
                                          (word_in_text('devils', tweet) and word_in_text('gewinnen', tweet))or
                                          (word_in_text('devils', tweet) and word_in_text('sieg', tweet))or
                                          (word_in_text('devils', tweet) and word_in_text('komm schon', tweet)) 
                                          
                                          )
tweets['lcfc'] = tweets['text'].apply(lambda tweet:
                                        (word_in_text('leicester', tweet) and word_in_text('win', tweet)) or
                                        (word_in_text('leicester', tweet) and word_in_text('vamos', tweet)) or
                                        (word_in_text('leicester', tweet) and word_in_text('bueno', tweet)) or
                                        (word_in_text('leicester', tweet) and word_in_text('hala', tweet)) or
                                        (word_in_text('leicester', tweet) and word_in_text('caray', tweet))or
                                        (word_in_text('leicester', tweet) and word_in_text('gewinnen', tweet))or
                                        (word_in_text('leicester', tweet) and word_in_text('sieg', tweet))or
                                        (word_in_text('leicester', tweet) and word_in_text('komm schon', tweet))or
                                        
                                        (word_in_text('lcfc', tweet) and word_in_text('win', tweet)) or
                                        (word_in_text('lcfc', tweet) and word_in_text('vamos', tweet)) or
                                        (word_in_text('lcfc', tweet) and word_in_text('bueno', tweet)) or
                                        (word_in_text('lcfc', tweet) and word_in_text('hala', tweet)) or
                                        (word_in_text('lcfc', tweet) and word_in_text('caray', tweet)) or
                                        (word_in_text('lcfc', tweet) and word_in_text('gewinnen', tweet))or
                                        (word_in_text('lcfc', tweet) and word_in_text('sieg', tweet))or
                                        (word_in_text('lcfc', tweet) and word_in_text('komm schon', tweet))
                                          
                                        )

print tweets['manutd'].value_counts()[True]
print tweets['lcfc'].value_counts()[True]

teams = ['manutd', 'lcfc']
tweets_by_teams = [tweets['manutd'].value_counts()[True], tweets['lcfc'].value_counts()[True]]

x_pos = list(range(len(teams)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_teams, width, alpha=1, color='g')

# Setting axis labels and ticks
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: manutd vs lcfc(raw data)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(teams)
plt.show()





