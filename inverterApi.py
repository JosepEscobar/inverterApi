import flask
import json
from app.data_source import DataSource

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>inverter API</h1> <p>Documentation about inverter API. (Work in progress)</p>"

@app.route('/configuration/', methods=['GET'])
def rating():
    rating = DataSource.getConfiguration()
    json = rating.toJSON()
    return json


@app.route('/status/', methods=['GET'])
def status():
    status = DataSource.getStatus()
    json = status.toJSON()
    return json

@app.route('/flag-status/', methods=['GET'])
def flagStatus():
    status = DataSource.getFlagStatus()
    json = status.toJSON()
    return json

app.run(host="0.0.0.0")