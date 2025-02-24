import os
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="datascore",
    version="0.1.0",
    description="API DataScore",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def read_root():
    return {'message': "Ecobe"}

# @app.get('/testando')
# def teste():
#     env = dict()
#     for key, value in os.environ.items():
#         env[key] = value

#     return {'message': env}
