from typing import List
from fastapi import Depends, FastAPI, Response,status,HTTPException

from blog import models, schemas

from database import SessionLocal, engine 
from sqlalchemy.orm import Session
from passlib.context import CryptContext


models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()
app=FastAPI()



pwd_cxt=CryptContext(schemes=["bcrypt"],deprecated="auto")


    
    
    


@app.post('/',status_code=201,tags=['blogs'])
def index(request:schemas.Blog,db:Session = Depends(get_db)):#because of req schema we have req body in swager doc
   
   new_blog=models.Blog(title=request.title,body=request.body)
   db.add(new_blog)
   db.commit()
   db.refresh(new_blog)
   
   return new_blog

@app.get('/blog',status_code=status.HTTP_200_OK,response_model=List[schemas.ShowBlog],tags=["blogs"])

def all(db:Session=Depends(get_db)):
    blogs=db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id1}',response_model=schemas.ShowBlog,tags=["blogs"])
def show(id1,response:Response,db:Session=Depends(get_db)):
    blogs=db.query(models.Blog).filter(models.Blog.id == id1).first()

    if not blogs:
        #response.status_code=status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} is not available')
    return blogs

@app.delete('/blog/{id1}',tags=["blogs"])
def destroy(id1,db:Session=Depends(get_db)):
        blog=db.query(models.Blog).filter(models.Blog.id == id1)
    
        if not blog.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id{id1} not found')
       
       
       
       
        blog.delete(synchronize_session=False)
        db.commit()
        return "Deleted the contain with id {id1}"



@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=["blogs"])

def update(id,request:schemas.Blog,db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id{id} not found')
    blog.update({'title':'updated title'})

    db.commit()
    return 'updated'







@app.post('/user',response_model=schemas.ShowUser,tags=["users"])
def create_user(request:schemas.User,db:Session = Depends(get_db)):
    hashedPassword=pwd_cxt.hash(request.password)
    new_user=models.User(name=request.name,mail=request.mail,password=hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user