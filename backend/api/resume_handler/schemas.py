from pydantic import BaseModel, Field, validator
from typing import Optional




class TunedModel(BaseModel):
    class Config:
        orm_mode = True



class GetResume(TunedModel):
    id:  int
    text: str
    

class RequestsResume(TunedModel):
    id:  int
 

