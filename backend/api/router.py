from fastapi import APIRouter
from api.get_data.router import get_data


api_router = APIRouter()
api_router.include_router(get_data, prefix='/api', tags=['api_v1'])
