#!/usr/bin/python3

import requests
import json

from netaddr import IPAddress, IPNetwork
from netaddr import AddrFormatError
from flask import Flask, request, abort
from flask_json import FlaskJSON, JsonError, json_response, as_json

#remove the InsecureRequestWarning messages
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

"""
api info
"""

app = Flask(__name__)
FlaskJSON(app)

@app.route('/hello')
def hello():
    debug = 1

    say_hello_json = {'message' : 'hello'}
    return(say_hello_json)
#end of hello

if __name__ == '__main__':
    app.run(host='0.0.0.0')