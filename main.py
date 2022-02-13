from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from api import animal_router
from data import AnimalList

animal_list = AnimalList()
app = FastAPI()


@app.get('/', tags=['main'], response_class=HTMLResponse)
def main():
    """
    View that shows description about the Animal API
    :return: A link to the API instructions
    """
    return """<a href="http://localhost:8000/docs">API instructions</a>"""


app.include_router(animal_router, prefix='/animals', tags=['animals'])
