from fastapi import FastAPI
from typing import Optional


app = FastAPI()


@app.get("/")
def index():
    dict= {"data": "blog list"}
    return dict

@app.get("/blog")
def getblogs(limit: int = 10, published: bool = True, sort: Optional[str]= None):
    
    if published:
        dict= {"data": f"{limit} published blogs from the database"}
    else:
        dict= {"data": f"{limit} no published blogs from the database"}
    return dict


@app.get("/blog/unpublished") #This must be before the "/blog/{blog_id}" path
def unpublished():
    return {"data": "all unpublished blogs"}

@app.get("/blog/{blog_id}")
def show_blog(blog_id: int):
    return {"data": blog_id}

@app.get("/blog/{blog_id}/comments")
def show_blog(blog_id: int):
    return {"data": f"{blog_id} commentary"}

@app.post("/blog")
def create_blog():
    return {"data": "Blog is created"}