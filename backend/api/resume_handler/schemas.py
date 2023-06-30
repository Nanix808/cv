from pydantic import BaseModel, Field, validator
from typing import List, Optional

class TunedModel(BaseModel):
    class Config:
        orm_mode = True

class Resume(TunedModel):
    id: int
    text: str

class GetResume(TunedModel):
    content: List[Resume]
    requirements: str
    
class RequestsResume(TunedModel):
    id:  int
 

