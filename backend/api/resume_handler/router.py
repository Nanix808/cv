from fastapi import APIRouter
from .schemas import GetResume
from .service import read_all_resume

resume_handler = APIRouter()

@resume_handler.post("/resume")
def range_resume(body: GetResume):
    return read_all_resume(body=body)
