from typing import Union
import uvicorn


from fastapi import FastAPI, APIRouter
from api.router import api_router

from sqlalchemy.ext.declarative import declarative_base


app = FastAPI(debug=True)

app.include_router(api_router)



if __name__ =="__main__":
    # uvicorn.run(app="main:app", reload=True, port=8080, host="0.0.0.0")
    uvicorn.run(app="main:app", host='127.0.0.1',  port=8000, reload=True)
