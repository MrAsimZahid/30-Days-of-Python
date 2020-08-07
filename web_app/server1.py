from flask import Flask
from web_scrapper_box_office import run as scrape_runner
app = Flask(__name__)

#ocalhost=http://0.0.0.0:8000/
@app.route("/", methods=['GET'])
def hello_world():
    return "this is a flask, server1"


@app.route("/box-office-mojo-scrapper", methods=['POST'])
def box_office_scraper_view():
    scrape_runner()
    return "done"