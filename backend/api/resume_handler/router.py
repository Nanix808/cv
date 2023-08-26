from fastapi import APIRouter
from .schemas import GetResume
import pandas as pd
from fastapi.responses import JSONResponse

from ml.text_models import text_job
from ml.text_preprocessing import PrepTransformer


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
    PrepTransform = PrepTransformer()
    resumes_df['text'] = resumes_df['text'].apply(PrepTransform.transform)
    target = PrepTransform.transform(target)

    #запускаем модель по логике cv
    range_id = text_job(data = resumes_df, target = target, how = 'cv')


    #запускаем модель по логике tfidf - это дает только печать индексов в терминале, не отображается на сайте
    range_id_tf = text_job(data = resumes_df, target = target, how = 'tfidf')


    range_cosine = text_job(data = resumes_df, target = target, how = 'cosine_similarity')


    result_dict = { 'Только важное'             :   {"range": range_id_tf[0], "accuracy" : range_id_tf[1]},
                    'Слово в слово'    :   {"range": range_id[0], "accuracy" : range_id[1]},
                    'Альтернативный взгляд'   :   {"range": range_cosine[0], "accuracy" : range_cosine[1]}
                  }

    return JSONResponse(content=result_dict)
