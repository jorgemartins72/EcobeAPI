from fastapi import FastAPI
import os
import json

app = FastAPI(
    title="datascore",
    version="0.1.0",
    description="API DataScore",
)

@app.get('/')
def read_root():

    env = dict()
    for key, value in os.environ.items():
        env[key] = value
    env['FOOFOOFOO'] = "BARBARBAR"

    # return {'message': env}
    return {'message': "Ecobe"}