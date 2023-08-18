import uvicorn


from fastapi import FastAPI
from api.router import api_router
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(debug=True)

app.include_router(api_router)

origins = ["*",
           "http://0.0.0.0:8080",
           "http://localhost:8080",
           "http://127.0.0.1:8080",
           "http://localhost:3000",
           
           ]

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
