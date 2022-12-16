import requests
from flask import json

req = requests.post('http://127.0.0.1:8000/reg')
print(req.text)