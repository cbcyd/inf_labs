from fastapi import FastAPI
import requests
from classes import *

app = FastAPI()


@app.get("/path/{title}")
async def with_path(title: str):
    '''Get summary of a Wikipedia page given the title'''

    # Send the request to Wikipedia's REST API
    r = requests.get(f'https://en.wikipedia.org/api/rest_v1/page/summary/{title}')

    if r.status_code == 200:
        data = r.json()

        # Create an Item with the title, URL, and summary of the page
        item = Item(title=title, url=data['content_urls']['desktop']['page'], summary=data['extract'])
        return item

    else: 
        return {"error": "Page not found"}


@app.get("/query/")
async def with_query(title: str):
    '''Query Wikipedia for a list of page titles'''

    # Define the parameters for the query
    params = {
        'action': 'query',
        'format': 'json',
        'list': 'search',
        'srsearch': title
    }

    # Send the request to Wikipedia's query service
    data = requests.get(f'https://en.wikipedia.org/w/api.php', params=params)

    if data.status_code == 200:
        data = data.json()

        # Generate a list of search result objects from the response data
        results = [SearchResult(title=i['title'], url=f'http://en.wikipedia.org/?curid={i["pageid"]}', snippet=rmspan(i['snippet'])) for i in data['query']['search']]
        search = Search(title=title, results=results)
        return search

    else: 
        return {"error": "Page not found"}


@app.post("/post/")
async def with_post(wiki: Wiki):
    '''Fetch pages related to the title of a Wikipedia page'''

    # Define the URL for the request
    url = f"https://en.wikipedia.org/api/rest_v1/page/related/{wiki.title}"

    # Send the request to Wikipedia's REST API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Extract data for each related page
        related_pages = []
        for page in data['pages']: 
            try:
                related_pages.append(RelatedPage(title=page['title'], url=page['content_urls']['desktop']['page'], description=page['description']))
            except:
                pass

        # Format the related pages as an ItemPost
        wiki = ItemPost(title=wiki.title, related_pages=related_pages)
        return wiki

    else: 
        return {"error": "Page not found"}