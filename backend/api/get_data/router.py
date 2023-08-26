from fastapi import APIRouter, Depends
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import ResumeCreate, ShowResume, Resume_Get_Id, UpdateResume, CreateShowResume
from api.database import get_db
from .service import ResumeDAL


get_data = APIRouter()

@get_data.get("/resume", response_model=list[ShowResume])
async def read_all_resume(db : AsyncSession = Depends(get_db))-> list[ShowResume]:
    async with db as session:
        async with session.begin():
            resume_dal = ResumeDAL(session)
            resume = await resume_dal.get_all_resume()
    return resume

@get_data.get("/resume/{resume_id}", response_model=ShowResume)
async def read_resume_by_id(resume_id, db : AsyncSession = Depends(get_db)) -> ShowResume:
    async with db as session:
        async with session.begin():
            resume_dal = ResumeDAL(session)
            resume = await resume_dal.get_resume_by_id(
                resume_id=resume_id,
              
            )
            return resume


@get_data.delete("/resume/del", response_model = Resume_Get_Id)
async def delete_resume(resume_id: int,  db: AsyncSession = Depends(get_db)) -> Resume_Get_Id:
    async with db as session:
        async with session.begin():
            resume_dal = ResumeDAL(session)
            resume = await resume_dal.delete_resume(resume_id=resume_id,)
            if not resume:
                raise HTTPException(
                status_code=404, detail=f"Резюме с таким id {resume_id} не найдено."
            )
        return Resume_Get_Id(id=resume_id)
  

@get_data.post("/resume/add", response_model=CreateShowResume)
async def create_resume(body: ResumeCreate, db : AsyncSession = Depends(get_db)) -> CreateShowResume:
    async with db as session:
        async with session.begin():
            resume_dal = ResumeDAL(session)

            resume_params = body.dict(exclude_none=True)
            resume = await resume_dal.create_resume(
                resume_params
            )
            return resume
   

@get_data.patch("/resume/update", response_model = Resume_Get_Id)
async def update_resume_by_id(resume_id: int, body: UpdateResume, db: AsyncSession = Depends(get_db)) -> Resume_Get_Id:
    updated_resume_params = body.dict(exclude_none=True)
    if updated_resume_params == {}:
        raise HTTPException(
            status_code=422,
            detail="Не предаставлены параметры для редактирования",
        )
    async with db as session:
        async with session.begin():
            resume_dal = ResumeDAL(session)
            resume = await resume_dal.update_resume(
                resume_id=resume_id,
                updated_resume_params=updated_resume_params
                   
            )
            if not resume:
                raise HTTPException(
                status_code=404, detail=f"Резюме с таким id {resume_id} не найдено."
            )
        return Resume_Get_Id(id=resume_id)
