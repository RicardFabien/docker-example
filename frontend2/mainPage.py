from flask import Flask
import requests
from requests import Session

app = Flask(__name__)

@app.route('/')
def test():
    session = Session()
    req = session.get('http://backend:80')
    return req.text

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=8888)