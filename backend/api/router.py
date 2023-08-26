from fastapi import APIRouter
from api.get_data.router import get_data
from api.resume_handler.router import resume_handler

api_router = APIRouter()

api_router.include_router(get_data, prefix='/api', tags=['api_v1'])
api_router.include_router(resume_handler, prefix='/api/v2', tags=['api_v2'])
