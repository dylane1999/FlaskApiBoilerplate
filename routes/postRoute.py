from app import app
from flask import request
from flask_api import status



@app.route("/post",  methods=['POST'])

def post(): 
      return (request.data)