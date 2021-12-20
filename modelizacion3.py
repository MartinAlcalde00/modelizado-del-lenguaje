# Natural Language Toolkit
import math
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
#Transition point
pt = math.sqrt(len(tokens))
#Create your n-grams
ugs = nltk.FreqDist(tokens)
bgs = nltk.bigrams(tokens)
fdist = nltk.FreqDist(bgs)

def medida(repeticiones, punto_transicion):
    medir = 1 / (abs(float(repeticiones) - punto_transicion) + 1)
    return medir

def take_second(elem):
    return elem[1]

con_medida = list()
search_word = 'encontrar'
sorted_by_second = sorted(fdist.items(), 
                          key = lambda tup: tup[1], reverse=True)

for k,v in sorted_by_second:
    if search_word in k[0]:
        for word2 in k[1]:
            if word2 != search_word:
                for w, freq in ugs.items():
                    if w == word2:
                        m = medida(freq, pt)
                        con_medida.append([k, m])

ordenados = sorted(con_medida, key = take_second, reverse = True)

#ordenados_sin_repeticion = list(dict.fromkeys(ordenados))
#print(ordenados_sin_repeticion)
        