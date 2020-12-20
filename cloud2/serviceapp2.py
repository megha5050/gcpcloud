import requests
import pprint
import flask
from flask import request, jsonify
host='0.0.0.0'
port='5000'
appdata=requests.get('http://localhost:3000/getip')
webpage=requests.get('http://localhost:3000')

pprint.pprint(appdata.json())
pprint.pprint(webpage.text)


caller_app=flask.Flask(__name__)



@caller_app.route('/', methods=['GET'])
def home_page():
    return ''' HELLO WORLD  '''


@caller_app.route('/masterapp/data',methods=['GET'])
def get_masterapi_data():
    return jsonify(appdata.json())


caller_app.run(host,port)
