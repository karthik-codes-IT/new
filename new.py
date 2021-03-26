import requests
from flask import Flask, jsonify,request

app = Flask(__name__)
@app.route('/', methods=["GET"])
def data():
    #return "karthik"
    response = requests.get(url="https://www.google.com/")
    #return response
    print(response.text)

if __name__ == "__main__":
    app.run()
