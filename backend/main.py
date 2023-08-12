import uvicorn


from fastapi import FastAPI
from api.router import api_router
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(debug=True)

app.include_router(api_router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ =="__main__":
    # uvicorn.run(app="main:app", reload=True, port=8080, host="0.0.0.0")
    uvicorn.run(app="main:app", host='0.0.0.0',  port=8000, reload=True)
