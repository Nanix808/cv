from pydantic import BaseModel, Field, validator
from typing import Optional
import uuid
from enum import Enum
from datetime import datetime, datetime


class Gender(Enum):
    none: float = None
    male: str = 'm'
    female: str = 'f'


class Education(Enum):
    none: float = None
    male = 'hight'
    female = 'low'



class TunedModel(BaseModel):
    class Config:
         orm_mode = True


class ResumeCreate(TunedModel):
    url: str = Field(max_length=128)
    source: str = Field(max_length=64, default='parsing')
    content: str = Field(max_length=16384)
    available : Optional[bool] 
    age: Optional[int]
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[Gender]
    education: Optional[Education]
    experience: Optional[str]
    skils: Optional[str]
    profession: Optional[str]
    languages: Optional[str]
    courses: Optional[str]
    computer_skils: Optional[str]


    class Config:  
        use_enum_values = True 





class ShowResume(TunedModel):
    id:  int
    url: str
    source: str
    content: str
    created_on: Optional[datetime]
    available : bool
    age: Optional[int]
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[str]
    education: Optional[str]
    experience: Optional[str]
    skils: Optional[str]
    profession: Optional[str]
    languages: Optional[str]
    courses: Optional[str]
    computer_skils: Optional[str] 


    @validator('content')
    def name_must_contain_space(cls, v):
        return v[:100]


class CreateShowResume(TunedModel):
    id: int
    url: str
    source: str
    content: str
    # created_on: Optional[datetime]
    available : bool
    age: Optional[int]
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[str]
    education: Optional[str]
    experience: Optional[str]
    skils: Optional[str]
    profession: Optional[str]
    languages: Optional[str]
    courses: Optional[str]
    computer_skils: Optional[str] 


    @validator('content')
    def name_must_contain_space(cls, v):
        return v[:100]


class Resume_Get_Id(TunedModel):
    id: Optional[int]
   


class UpdateResume(TunedModel):
    name : Optional[str]
    url: Optional[str]
    source: Optional[str]
    content: Optional[str]
