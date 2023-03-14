from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app=FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'sourabh'}}


@app.get('/show/{id}')
def show(id):
    return {'data':id}

@app.get('/showint/{id1}')
def show(id1: int):
    return {'data':id1}


@app.get('/blogs/') #/blog?limit=50&published=false
def show(limit=10,published:bool=True,sort:Optional[str]=None):
    if published:
     return {'data':limit}

    else :
        return limit

class blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]


@app.post('/blog')
def show(request:blog):#u can call it with any name
  return {'data':f"blog is created with title' {request.title}"}


if __name__=="__main__":
    uvicorn.run(app,host='127.0.0.1',port='8000')
