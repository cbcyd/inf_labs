from pydantic import BaseModel
from typing import List


class Item(BaseModel):
    title: str
    url: str
    summary: str

class Wiki(BaseModel):
    title: str

class Search(BaseModel):
    title: str
    results: list

class SearchResult(BaseModel):
    title: str
    url: str
    snippet: str

class RelatedPage(BaseModel):
    title: str
    url: str
    description: str

class ItemPost(BaseModel):
    title: str
    related_pages: List[RelatedPage]

def rmspan(s):
    s = s.replace('<span class=\"searchmatch\">', '')
    s = s.replace('</span>', '')
    return s