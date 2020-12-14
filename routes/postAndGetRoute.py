from app import app
from flask import request


@app.route("/postandget", methods=['POST', 'GET'])

def postandget():
    if request.method == "GET":
        return ({'hello': "world"})
    else:
        pass
        return (request.data)
