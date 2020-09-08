#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Essentials
import re
import pandas as pd
from collections import Counter
count_by_comment = Counter()
from nltk.corpus import stopwords

# NLTK 
import nltk
from nltk.stem.porter import *
from nltk.corpus import stopwords
from nltk.util import ngrams
from nltk.stem import WordNetLemmatizer
stemmer = PorterStemmer()

### Set up and Functions ###
### add any other stopword you want
class SearchCounter(object):
    stop = stopwords.words('english')
    def __init__(self, data, keyword, volume, numbers, **kwargs):
        self.data = data
        self.keyword = keyword
        self.volume = volume
        self.numbers = numbers    
    def text_processing(self, text):
        temp =[]
        final = []
        lemon = WordNetLemmatizer()
        for sentence in text:
            sentence = sentence.lower()
            cleanr = re.compile('<.*?>')
            sentence = re.sub(cleanr, ' ', sentence)
            sentence = re.sub(r'[?|!|\'|"|#]',r'',sentence)
            sentence = re.sub(r'[.|,|)|(|\|/]',r'',sentence)
            sentence = re.sub("[\(\[].*?[\)\]]", "", sentence)

            words = [lemon.lemmatize(word) for word in sentence.split() if word not in self.stop]   # Removing stopwords and lemmatization
            temp.append(words)

        for row in temp:
            sequ = ''
            for word in row:
                sequ = sequ + ' ' + word
            final.append(sequ)
        return final
    
    def add_stopwords(self, terms, **kwargs):
        global stop
        self.stop += terms
        
    def count_keywords(self):
        num_comm = self.numbers 
        text_data = self.text_processing(text=self.data[self.keyword])
        for text in text_data: 
            token_list = re.findall("[a-z]{3,}",text.lower()) 
            # Keep specific pattern of the text and return tokenized keywords
            # Add special symbol you want to keep in "[]" (i.e.[a-z'@#&])
            # Select how many characters of keyword and above you want to return
            stop_words_remove = [element for element in token_list if element not in self.stop]
            stop_words_remove_unique = Counter(stop_words_remove)
            for i in stop_words_remove_unique:
                count_by_comment[i] +=1
        volume = []
        for collect in count_by_comment.most_common(num_comm):
            root_term = collect[0]
            df_segment = self.data[self.data[self.keyword].str.contains(root_term)]
            search_volume = df_segment[self.volume].sum()
            volume.append(search_volume)
        master_count = pd.DataFrame(count_by_comment.most_common(num_comm), columns=['Keyword', 'Frequency of Mentions'])
        master_count['Attributed Search Volume'] = volume     
        master_count = master_count[['Keyword', 'Attributed Search Volume', 'Frequency of Mentions']]        
        master_count = master_count.sort_values(by=['Attributed Search Volume'], ascending=False)
        return master_count

