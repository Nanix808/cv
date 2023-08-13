def text_preprocessing(text: str) -> str:    
    return text

# Необходима библиотека nltk 3.8.1
# Предварительно необходимо скачать такую модель
# через cmd такая строка: python -m spacy download ru_core_news_md

from nltk.stem import SnowballStemmer
import spacy
from stop_words import stop_words


class PrepTransformer():

    def __init__(self, how="lemma") -> None:
        """Параметр how определяет выбор способа подготовки токенов:
        - 'lemma' -> используется лемматизация
        - 'stem' -> используется стемминг
        - None -> не применяется ни один из способов"""
        self.how = how
        #Загружаем модель из библиотеки spacy для токенизации и лемматизации
        self.nlp = spacy.load('ru_core_news_md')
        self.stop_words = stop_words
    
        #Делаем трансформер для стемминга
        self.SBstemmer = SnowballStemmer("russian")
        

    def transform(self, text: str)-> str:
        #Создаем nlp-transfprmer
        self.doc = self.nlp(text)
    
        #Используем метод лемматизации (токенизация, приведение к ниж. регистру и лематизация происходит в рамках одной модели)
        # и делаем проверку на стоп-слова
        if self.how == 'lemma':
            self.tokens = [w.lemma_ for w in self.doc if (w.pos_!='SPACE') and (w.pos_!='PUNCT')]
            self.filtered_tokens = [token for token in self.tokens if token not in self.stop_words]
            return ' '.join(self.filtered_tokens)
    
        #Если выбрали не лемматизацию, то делаем токенизацию, приведение к нижнему регистру, проверку на стоп-слова
        else:
            self.tokens = [w.text for w in self.doc if (w.pos_!='SPACE') and (w.pos_!='PUNCT')]
            self.tokens_low = [token.lower() for token in self.tokens]
            self.filtered_tokens = [token for token in self.tokens_low if token not in self.stop_words]
    
            #Делаем стемминг каждого токена
            if self.how == 'stem':
                self.SBstems = [self.SBstemmer.stem(token) for token in self.filtered_tokens]
                return ' '.join(self.SBstems)
    
            #Возвращаем токены без изменений
            else:
                return ' '.join(self.filtered_tokens)
            
