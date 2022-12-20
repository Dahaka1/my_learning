from flask import Flask
from flask import request

app = Flask(__name__)

dictionary = {}

@app.route('/users/<user_id>', methods = ['GET', 'POST', 'DELETE'])
def user(user_id):
    if request.method == 'GET':
        return dictionary[user_id] if dictionary[user_id] else 'Do you wanna create a user?'

    if request.method == 'POST':
        """modify/update the information for <user_id>"""
        # you can use <user_id>, which is a str but could
        # changed to be int or whatever you want, along
        # with your lxml knowledge to make the required
        # changes
        data = request.form # a multidict containing POST data

    if request.method == 'DELETE':
        """delete user with ID <user_id>"""

    else:
        return 405
        # POST Error 405 Method Not Allowed

app.run()