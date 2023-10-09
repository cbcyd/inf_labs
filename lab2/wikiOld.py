from fastapi import FastAPI
from pydantic import BaseModel
import wikipedia

app = FastAPI()

class Item(BaseModel):
    title: str
    summary: str

class Wiki(BaseModel):
    title: str

@app.get("/path/{title}") 
async def with_path(title: str):
    page = wikipedia.page(title)
    item = Item(title=page.title, summary=wikipedia.summary(title))
    return item

@app.get("/query/")
async def with_query(title: str):
    page = wikipedia.page(title)
    item = Item(title=page.title, summary=wikipedia.summary(title))
    return item

@app.post("/post/")
async def with_post(wiki: Wiki):
    page = wikipedia.page(wiki.title)
    wiki = Item(title=page.title, summary=wikipedia.summary(wiki.title))
    return wiki