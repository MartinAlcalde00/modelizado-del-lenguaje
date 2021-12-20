# Natural Language Toolkit
import nltk
from nltk.corpus import stopwords

stopwords = stopwords.words('spanish')
def conditioning_file(file_name):
        huge_list = [] 
        with open(file_name, "r") as f:
            huge_list = f.read().split()
        huge_list_no_stopwords = [word.lower() for word in huge_list
                         if word.lower() not in stopwords]
        text_no_stopwords = ' '.join(huge_list_no_stopwords).replace('.', '').replace(',', '')
        return text_no_stopwords
    
tokens = nltk.word_tokenize(conditioning_file('test.txt'))

#Create your bigrams
bgs = nltk.bigrams(tokens)
fdist = nltk.FreqDist(bgs)

#Search and frequencies
sorted_by_second = sorted(fdist.items(), 
                          key = lambda tup: tup[1], reverse = True)
search_word = 'encontrar'
for k,v in sorted_by_second:
    if search_word in k[0]:
        print(k,v)
    else:
        None
        