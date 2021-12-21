import math
import nltk
from nltk.corpus import stopwords

stopwords = stopwords.words('english') #opcional con el método del punto de transición
def remove_symbols(str):
    str1 = str.replace('.', '').replace(',', '').replace(';', '')
    str2 = str1.replace('(', '').replace(')', '').replace('"', '')
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

# Create your n-grams
ugs = nltk.FreqDist(tokens)
bgs = nltk.bigrams(tokens)
fdist = nltk.FreqDist(bgs)
# punto de transición
pt = math.sqrt(len(ugs))

def medida(repeticiones, punto_transicion):
    medir = 1 / (abs(float(repeticiones) - punto_transicion) + 1)
    return medir

def take_second(elem):
    return elem[1]

con_medida = list()
search_word = 'body' #palabra intruducida
for k, v in fdist.items():
    if search_word in k:
        for word2 in k:
            if (word2 != search_word) and (search_word == k[0]):
                for w, times in ugs.items():
                    if w == word2 :
                        m = medida(times, pt)
                        con_medida.append([k, m])


ordenados = sorted(con_medida, key = take_second, reverse = True)
for i in range(len(ordenados)):
    print(ordenados[i])

