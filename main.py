from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/', methods=["GET"])
def getData():
    try:
        with open("./users.json", "r") as file:
            data = json.load(file)

        return data
    except Exception as err:
        return err

if __name__ == '__main__':
    app.run()
