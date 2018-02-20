import read
from collections import Counter

#import and read previously defined dataframe
data = read.load_data()

#combine all the headlines into one long string, lowercase every words, then split into a list of words
headlines = data['headline']
new_headline = ''
for hd in headlines:
    new_headline += (' ' + str(hd))

split_headline = new_headline.lower().split()

#create a counter to count the occurences of each word
counted = Counter(split_headline)

#find the top 100 most frequently appeared words
top100 = counted.most_common(100)
print(top100)