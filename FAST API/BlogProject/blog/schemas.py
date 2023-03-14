from pydantic import BaseModel





class User(BaseModel):
    name:str
    mail:str
    password:str




class ShowBlog(BaseModel):
    title:str
    class Config():#for response 
        orm_mode=True


class ShowUser(BaseModel):
    name:str
    mail:str
    blog:list[ShowBlog]
    class Config():#for response 
        orm_mode=True


class Blog(BaseModel):
    title:str
    body:str
    creator:ShowUser