import flask
import json
from app.data_source import DataSource

app = flask.Flask(__name__)
app.config["DEBUG"] = True
dataSource = DataSource()

@app.route('/', methods=['GET'])
def home():
    return "<h1>inverter API</h1> <p>Documentation about inverter API. (Work in progress)</p>"

@app.route('/configuration/', methods=['GET'])
def rating():
    rating = dataSource.getConfiguration()
    json = rating.toJSON()
    return json


@app.route('/status/', methods=['GET'])
def status():
    status = dataSource.getStatus()
    json = status.toJSON()
    return json

@app.route('/flag-status/', methods=['GET'])
def flagStatus():
    status = dataSource.getFlagStatus()
    json = status.toJSON()
    return json

app.run(host="0.0.0.0")