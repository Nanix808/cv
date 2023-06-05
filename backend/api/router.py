from fastapi import APIRouter
# from getdata1.router import getdata1

from api.get_data.router import get_data




api_router = APIRouter()

api_router.include_router(get_data, prefix='/api', tags=['api_v1'])




# async def _create_new_user(body: UserCreate, session):
#     async with async_session() as session:
#         async with session.begin():
#             user_dal = UserDAL(session)
#             user = await user_dal.create_user(
#                 name=body.name,
#             )
#             return 'user_dal'



# @api_v1.post("/user")
# async def create_user(body: UserCreate):
#     return await _create_new_user(body)

# @api_router.get("/")
# def read_root():
#     return {"Hello": "World1"}