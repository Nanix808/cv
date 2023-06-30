from fastapi import APIRouter
from .schemas import GetResume
from random import sample


resume_handler = APIRouter()

@resume_handler.post("/resume")
def read_all_resume(body: GetResume):
    resume_params = body.dict(exclude_none=True)
    # print(resume_params['requirements']) # Тут приходят требования вида str(просто текст)
    # print(len(resume_params['content'])) # Тут приходит контетн вида [ {id:1, text:'текст резюме1'}, {id:2, text:'текст резюме2'}]
    id_resume = list(map(lambda x: x['id'], resume_params['content'])) # получаю пришедшие id
    # print(id_resume)
    range_id = sample(id_resume, len(id_resume)) # сортирую  id иметируя ранжирование
    return range_id

