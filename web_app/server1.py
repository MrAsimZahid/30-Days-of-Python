from flask import Flask
from logger import trigger_log_save
from web_scrapper_box_office import run as scrape_runner
app = Flask(__name__)

#ocalhost=http://0.0.0.0:8000/
@app.route("/", methods=['GET'])
def hello_world():
    return "this is a flask, server1"

#ocalhost=http://0.0.0.0:8000/
@app.route("/abc", methods=['GET'])
def abs():
    return "abc function"


@app.route("/box-office-mojo-scrapper", methods=[' POST'])
def box_office_scraper_view():
    trigger_log_save()
    scrape_runner()
    return "done"