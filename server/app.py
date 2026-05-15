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
ROUTE 1: Create the homepage index route for the app and provide the appropriate decorator. Set up the host, appname, and response body. Make sure we include the a href to redirect the user to the proper link to access the approproutes needed.
"""
@app.route('/')
def index():
    # Create the host header sent by the client
    host = request.headers.get("Host")

    # Create a name for Flask to assign to the application
    appname = current_app.name

    # Create a simple HTML page to display to the user
    response_body = f"""
        <h1> The host for this page is {host}</h1>
        <h2> The name for this application is {appname}</h1>
        <h3> The path of this application on the user's device is {g.path}</h3>
        <h3><a href="/contract/1">View Contract 1</a></h3>
        <h3><a href="/customer/bob">Verify customer: Bob</a></h3>
    """

    # Set the status code of OK and return data
    status_code = 200

    # No custom headers needed at this route
    headers = {}

    return make_response(response_body, status_code, headers)


"""
ROUTE 2: Create the route to display contacts, make sure to display status 200-OK if found and 404 if not. Also provide the route decorator.

Create a function to take the id parameter to look for the contract by id. The contract id will be sent in the URL path. Provide redirection and flow for the program if the contract is found or not.
"""
@app.route('/contract/<int:id>')
def contract_info(id):
    """
    Use the next method to return the first contract match and none if it isn't found.

    Use a generator expression to search the contract list for the dictionary id that matches.
    """
    contract = next((c for c in contracts if c["id"] == id), None)
    
    # Control flow for the application
    if contract:
        response_body = contract['contract_information']
        status_code = 200
    else:
        response_body = f"There is no contract found with that {id}, try again."
        status_code = 404
    return make_response(response_body, status_code)


"""
ROUTE 3: Create the route for the customers. Make sure to not disclose any data respond with responding witha a 204 if the customer exists and 400 if otherwise. To ensure this do not include anything in the body. Make sure to provide the proper route decorator.

Create a function to take the customer name as a parameter to look for the customer by name. The customer name will be sent in the URL path. Provide redirection and flow for the program if the customer is found or not.
"""
@app.route('/customer/<customer_name>')
def customer_info(customer_name):
    """
    Make sure to verify if a customer exists or not, and do not disclose any data in the process. We need to verify if the customer name matches in the lowercase form.
    """
    if customer_name.lower() in customers:
        response_body = ""
        status_code = 204
    else:
        response_body = f"Customer {customer_name} not found."
        status_code = 404
    
    return make_response(response_body, status_code)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
