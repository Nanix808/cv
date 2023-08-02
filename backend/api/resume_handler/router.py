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

    result_dict = {'TF-IDF': range_id_tf, 'CountVectorizer': range_id, 'TF-IDF1': range_id_tf}

    return JSONResponse(content=result_dict)


    #print(type(resumes_df))
    #print(resumes_df, target)
    #нужно распаковать все резюме в датафрейм
    #print('Требования ', resume_params['requirements']) # Тут приходят требования вида str(просто текст)
    #print('Поступило резюме - ', len(resume_params['content'])) # Тут приходит контетн вида [ {id:1, text:'текст резюме1'}, {id:2, text:'текст резюме2'}]
    #id_resume = list(map(lambda x: x['id'], resume_params['content'])) # получаю пришедшие id
    #print('первичный порядок', id_resume)
    #range_id = sample(id_resume, len(id_resume)) # сортирую  id иметируя ранжирование
    #print('сортировка', range_id)
    #return range_id

