#!/usr/bin/env python3
import os
from flask import Flask, request, current_app, g, make_response

contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"}
]

customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

"""
Provide this hook which runs a function before each request so that our views know where the application is located. The absolute path will be stored in g.path so that it is avaiable to all routes so it doesn't need to be recalculated each time
"""
@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

"""
ROUTE 1: Create the index route for the app provide the appropriate decorator. Set up the host, appname, and response body if needed.
"""
@app.route('/')
def index():

"""
ROUTE 2: Create the route for the contacts do not disclose any data respond with 204. Also list the route decorator.
"""
@app.route('/contract/<id>')
def contractor_info():


"""
ROUTE 3: Create the route for the customers do not disclose any data respond with 204.
"""
@app.route('/customer/<customer_name>')
def customer_info():
  

if __name__ == '__main__':
    app.run(port=5555, debug=True)
