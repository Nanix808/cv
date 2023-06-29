from fastapi import APIRouter
from .schemas import GetResume


resume_handler = APIRouter()

@resume_handler.post("/resume")
def read_all_resume(body: GetResume):
    resume_params = body.dict(exclude_none=True)
    print(resume_params['requirements'])
    print(len(resume_params['content']))
    return {'w':3}

