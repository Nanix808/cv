from typing import Literal, List
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity

#переменная для выбора способа работы с резюме
HOW = Literal["cv", "tfidf", "cosine_similarity"]

def text_job (data: pd.DataFrame, target: str, how: HOW) -> List:
    
    '''
    Функция для сортировки резюме
    Важно получить на вход датафрейм с колонками 'text' и 'id', требования как string и один из двух методов обработки
    в результате получается список с ранжированными индексами поступивших резюме
    '''

    #создаем объект векторайзер
    cv = CountVectorizer()
    #применяем фит_трансформ ко всем резюме и трансформ к требованиям
    matrix = cv.fit_transform(data['text'])
    vector = cv.transform([target]).T
    
    #перемножаем получившиеся матрицу с вектором требований
    find_cv = matrix @ vector

    #создаем объект tfidf
    tfidf_transformer = TfidfTransformer()
    
    #применяем фит_трансформ к уже сформированной матрице
    tfidf_matrix = tfidf_transformer.fit_transform(matrix)
    #перемножаем получившиеся матрицу с вектором требований
    find_tfidf = tfidf_matrix @ vector

    #cosine similarity
    cos_matrix = tfidf_matrix.toarray()
    cos_vector = cv.transform([target]).toarray()
    res_matrix = np.append(cos_matrix, cos_vector, axis=0)
    res=cosine_similarity(res_matrix)

    #ставим баллы каждому резюме
    data['score_cv'], data['score_tfidf'] = find_cv.A[:,0], find_tfidf.A[:,0]

    if how == "cv":
        return list(data.sort_values('score_cv', ascending=False)['id'])
    elif how == "tfidf":
        return list(data.sort_values('score_tfidf', ascending=False)['id'])
    elif how == "cosine_similarity":
        return res[-1,:].argsort().tolist()







