
from fastapi import FastAPI
from pydantic import BaseModel
from wikipediaapi import Wikipedia

app = FastAPI()

wiki_wiki = Wikipedia('MyProjectName (merlin@example.com)', 'en')

class Item(BaseModel):
    title: str
    summary: str
    #text: str

class Wiki(BaseModel):
    title: str

@app.get("/path/{title}") 
async def with_path(title: str):
    page_py = wiki_wiki.page(title)
    #wiki = Wiki(title=page_py.title, summary=page_py.summary, text=page_py.text)
    item = Item(title=page_py.title, summary=page_py.summary)#, text=page_py.text)
    #return {"Summary:": wiki.summary} if page_py.exists() else 'Page not found'
    return item

@app.get("/query/")
async def with_query(title: str):
    page_py = wiki_wiki.page(title)
    #wiki = Wiki(title=page_py.title, summary=page_py.summary, text=page_py.text)
    item = Item(title=page_py.title, summary=page_py.summary)#, text=page_py.text)
    #return {"Title:": wiki.title, "Summary:": wiki.summary, "Text": wiki.text} if page_py.exists() else 'Page not found'
    return item

@app.post("/post/")
async def with_post(wiki: Wiki):
    page_py = wiki_wiki.page(wiki.title)
    wiki = Item(title=page_py.title, summary=page_py.summary)#, text=page_py.text)
    return wiki
