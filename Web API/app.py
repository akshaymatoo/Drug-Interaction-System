#!flask/bin/python
from flask import Flask, jsonify
from restAPI import Pymg

app = Flask(__name__)

@app.route('/api/v1/drugs/<string:name>', methods=['GET'])
def get_tasks(name):
    rest_api = Pymg()
    return jsonify(rest_api.getData(name))

if __name__ == '__main__':
    app.run('0.0.0.0')
