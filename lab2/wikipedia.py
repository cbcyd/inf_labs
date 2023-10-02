# Import required libraries
from fastapi import FastAPI
from pydantic import BaseModel, Field
from wikipediaapi import Wikipedia

# Initialize FastAPI app
app = FastAPI()

# Create an instance of wikipedia object
wikipedia = Wikipedia('User-Agent: CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org) generic-library/0.0', "en")

# Pydantic model for input validation
class RequestModel(BaseModel):
    path: str = Field(...)

# Endpoint to get Wikipedia data using path
@app.get("/path/{path}")
async def get_info_path(path: str):
    page_py = wikipedia.page(path)
    return {"page": page_py.text}

# Endpoint to get Wikipedia data using query
@app.get("/query/")
async def get_info_query(query: str):
    page_py = wikipedia.page(query)
    return {"page": page_py.text}

# Pydantic model for input validation
class BodyParams(BaseModel):
    body_param: str

# Endpoint to get Wikipedia data using body params
@app.post("/body/")
async def post_info_body(body_params: BodyParams):
    page_py = wikipedia.page(body_params.body_param)
    return {"page": page_py.text}