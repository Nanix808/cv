from typing import List
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from fastapi.responses import JSONResponse

def text_work (data: List[str]):
    
    '''
    Функция для сортировки резюме

    '''

    cv = CountVectorizer(stop_words='english')

    matrix = cv.fit_transform(data[:-1])

    vector = cv.transform([data[-1]])

    vector_t = vector.T



    find_cv = matrix @ vector_t

    cv = find_cv.A[:,0]



    tfidf_transformer = TfidfTransformer()

    tfidf_matrix = tfidf_transformer.fit_transform(matrix)

    find_tfidf = tfidf_matrix @ vector_t

    tfidf=find_tfidf.A[:,0]



    cos_matrix = matrix.toarray()

    res=cosine_similarity(cos_matrix, vector)

    cosine = np.array([item for sublist in res for item in sublist])


    scaler = MinMaxScaler()

    def to_screen(array: np.ndarray) -> List:
        
        array_idx = np.argsort(array)[::-1]+1

        list_idx = array_idx.tolist()

        array_scaled = scaler.fit_transform(np.sort(array).reshape(-1, 1)[::-1])*100

        list_scaled = array_scaled.ravel().round(2).tolist()

        return [list_idx, list_scaled]
    

    result_dict = { 'Только важное'           :   {"range": to_screen(tfidf)[0],     "accuracy" : to_screen(tfidf)[1]},
                    'Слово в слово'           :   {"range": to_screen(cv)[0],  "accuracy" : to_screen(cv)[1]},
                    'Альтернативный взгляд'   :   {"range": to_screen(cosine)[0], "accuracy" : to_screen(cosine)[1]}
                  }

    return JSONResponse(content=result_dict)
