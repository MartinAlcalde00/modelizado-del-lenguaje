# Natural Language Toolkit
import nltk
from nltk.corpus import stopwords

stopwords = stopwords.words('english')
def remove_symbols(str):
    str1 = str.replace('.', '').replace(',', '').replace(';', '')
    str2 = str1.replace('(', '').replace(')', '').replace('``', '')
    return str2
def conditioning_file(file_name):
        huge_list = [] 
        with open(file_name, "r") as f:
            huge_list = f.read().split()
        huge_list_no_stopwords = [word.lower() for word in huge_list
                         if word.lower() not in stopwords]
        text_no_stopwords = remove_symbols(' '.join(huge_list_no_stopwords))
        return text_no_stopwords
    
tokens = nltk.word_tokenize(conditioning_file('kafka.txt'))

#Create your bigrams
bgs = nltk.bigrams(tokens)
fdist = nltk.FreqDist(bgs)

#Search and frequencies
sorted_by_second = sorted(fdist.items(), 
                          key = lambda tup: tup[1], reverse = True)
search_word = 'body'
for k,v in sorted_by_second:
    if search_word in k[0]:
        print(k,v)
    else:
        None
        
        
        