from nltk.tokenize import sent_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import lancaster
from nltk import word_tokenize
import re
from nltk.chunk import RegexpParser
from nltk import sent_tokenize
import nltk
import spacy
import os
from nltk.corpus import stopwords
import string
from collections import Counter
import nltk
import collections 
import string
#root_dir="C://Users//r-naveenj//Desktop//tasks//temp_task2//"
fileName="C://Users//r-naveenj//Desktop//contracts//data//sample_data.txt"

#common set of functions and preprocesssing for all tasks 
def read_file(fileName): #reading file 
    input_file = open(fileName,'r+',encoding='utf8')
    return input_file.read()
def sent_split(input_file):# sentence tokenization
    sentence = read_file(input_file) #calling the readfile_fuction
    return sent_tokenize(sentence)
def remove_whitespace(text): #function to remove white space
    return  " ".join(text.split()) 
def remove_punctuation(text): #function removing punctuation
    translator = str.maketrans('', '', string.punctuation) 
    return text.translate(translator) 
def sent_normalize(text):# sentence normalization function
    #text=list_text(text)
    text = remove_punctuation(text)
    text = remove_whitespace(text)
    return text
def remove_stopwords(sent,is_lower_case=False):
    tokens=word_tokenize(sent)
    stopword_set = set(stopwords.words("english"))
    #if is_lower_case:
    filtered_tokens = [token.lower() for token in tokens
                      if token.lower() not in stopword_set and len(token) >= 2]
    filtered_text = ' '.join(filtered_tokens) 
    return filtered_text
def remove_special_characters(text):
    if re.findall(r'\w+', text):
        pattern = r'[^a-zA-z0-9\s]'
        text = re.sub(pattern, '', text)
    return text

    if re.findall(r'\w+', text):
        pattern = r'[^a-zA-z0-9\s]'
        text = re.sub(pattern, '', text)
    return text


def chunking_noun(document):
    #Get the words in the document
    words = word_tokenize(document)
    tagged = nltk.pos_tag(words)
    counts = Counter( tag for WORD,  tag in tagged)
    counts=dict(counts)
    #print(counts)
    chunkGram = r""" PHRASE: {(<JJ>* <NN.*>+ <IN>)? <JJ>* <NN.*>+}"""
    chunkParser = RegexpParser(chunkGram)
    chunked = chunkParser.parse(tagged)
    serch_keywords = []
    for tree in chunked.subtrees():
        if tree.label() == 'PHRASE':
            serch_keyword = ' '.join([x for x,y in tree.leaves()])
            serch_keywords.append(serch_keyword)
    serch_keywords = [w for w in serch_keywords if len(w.split(' ')) > 1 and  len(w.split(' ')) <=3 ] 
    return serch_keywords,tagged,counts

if fileName.endswith('.txt'):

    splited_sentences = sent_split(fileName) #sentence tokennize function calling
    #wring flies specific to the folder 
    #writeFile = open(self.dirname+folder_name+"//"+"POStage"+"--"+str(folder_name)+".tsv", 'a')
    #if file==first_file:
        #  writeFile.write("folder_name"+"\t"+ "page_NO"+"\t"+"sentence_id"+"\t"+"pos_sent"+"\t"+"noun_pharse_sent"+"\n")

    for each_sentence in splited_sentences:
        each_sent=sent_normalize(each_sentence)
        each_sent=remove_stopwords(each_sent)
        each_sent=remove_special_characters(each_sent)
        noun_pharse_sent,pos_sent,count1=chunking_noun(each_sent)
        print(noun_pharse_sent)
        
