def text_preprocessing(text: str) -> str:    
    return text

# Необходима библиотека nltk 3.8.1
# Необходима библиотека pymorphy2  0.9.1
# Необходима библиотека pymorphy2-dicts-ru  2.4.417127.4579844

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import download as nltk_download
from nltk.stem.snowball import SnowballStemmer
from string import punctuation
import pymorphy2


class PrepTransformer():

    def __init__(self, how="stem") -> None:
        """Параметр how определяет выбор способа подготовки токенов:
           - 'lemma' -> используется лемматизация
           - 'stem' -> используется стемминг
           - None -> не применяется ни один из способов"""
        self.how = how
        
        #Необходимо для использования word_tokenize для выделения из текста токенов
        nltk_download('punkt')

     
        #Исключаем стоп-слова, знаки препинания, иные знаки
        nltk_download('stopwords') 
        self.russian_stopwords = stopwords.words("russian") 
        self.punkt_list = [punctuation[n] for n in range(len(punctuation))] 
        self.punkt_list.extend(['...', '—', '``', "''", '“', '”', "«", "»"]) 
        self.russian_stopwords.extend(self.punkt_list) 
        self.stop_words = set(self.russian_stopwords) 
        

        #Делаем лемматизацию
        # self.morph = pymorphy2.MorphAnalyzer() 
        

        #Делаем стемминг
        self.stemmer = SnowballStemmer("russian") 
        

    
    def transform(self, text):
        
        #При помощи библиотеки nltk делаем токенизацию (отдельные знаки препинания становятся отдельными токенами)
        self.tokens = word_tokenize(text, language="russian")

        #Приводим весь текст к нижнему регистру
        self.tokens = [token.lower() for token in self.tokens]

        #Исключаем стоп-слова, знаки препинания, иные знаки
        self.filtered_tokens = [token for token in self.tokens if token not in self.stop_words]

        #Делаем лемматизацию
        # self.lemmas = [self.morph.parse(token)[0].normal_form for token in self.filtered_tokens]

        #Делаем стемминг
        self.stems = [self.stemmer.stem(token) for token in self.filtered_tokens]

        #Возвращаем токены в строку
        if self.how == 'lemma':
            return ' '.join(self.lemmas)
        
        elif self.how == 'stem':
            return ' '.join(self.stems)
        
        elif self.how == None:
            return ' '.join(self.filtered_tokens)
        
