import json
from fastapi import APIRouter
from .schemas import GetResume
import pandas as pd
from fastapi.responses import JSONResponse
#импорт двух новых функций из МЛ
from ml.text_models import text_job
from ml.text_preprocessing import text_preprocessing


resume_handler = APIRouter()

@resume_handler.post("/resume")
def read_all_resume(body: GetResume):
    #распаковали поступившие резюме и требования
    resume_params = body.dict(exclude_none=True)
    
    #создали датафрейм из резюме
    resumes_df = pd.DataFrame(resume_params['content'], columns = ['id', 'text'])

    #создали переменную поиска из требований
    target = resume_params['requirements']
    
    #нормализация текста - пока пустая
    resumes_df['text'] = resumes_df['text'].apply(text_preprocessing)
    target = text_preprocessing(target)

    #запускаем модель по логике cv
    range_id = text_job(data = resumes_df, target = target, how = 'cv')
    print(range_id)

    #запускаем модель по логике tfidf - это дает только печать индексов в терминале, не отображается на сайте
    range_id_tf = text_job(data = resumes_df, target = target, how = 'tfidf')
    print(range_id_tf)

    range_cosine = text_job(data = resumes_df, target = target, how = 'cosine_similarity')

    result_dict = {'TF-IDF': {"range": range_id_tf, "prc" : prc}, 'CountVectorizer': range_id, 'CosineSimilarity': range_cosine}

    return JSONResponse(content=result_dict)


