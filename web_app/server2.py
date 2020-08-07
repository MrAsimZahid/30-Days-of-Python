from fastapi import FastAPI
from web_scrapper_box_office import run as scrape_runner
app = FastAPI()

@app.get("/")
def hello_world():
    return {"hello : world"}


@app.post("/box-office-mojo-scrapper")
def scrape_runner_view():
    scrape_runner()
    return {"hello : world"}