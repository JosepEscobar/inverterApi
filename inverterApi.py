import flask
import json
from app.data_source import DataSource

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1> <p>A prototype API for distant reading of science fiction novels.</p>"


@app.route('/rating/', methods=['GET'])
def rating():
    rating = DataSource.getRating()
    json = rating.toJSON()
    return json
    #return "<h1>Distant Reading Archive</h1> <p>A prototype API for distant reading of science fiction novels.</p>"


@app.route('/status/', methods=['GET'])
def status():
    status = DataSource.getStatus()
    json = status.toJSON()
    return json
    #return "<h1>Distant Reading Archive</h1> <p>A prototype API for distant reading of science fiction novels.</p>"


app.run(host="0.0.0.0")