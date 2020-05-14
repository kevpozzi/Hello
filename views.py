from flask import Blueprint, jsonify, make_response

from src.hello.service.helloService import helloService

hello_api = Blueprint('hello_api', __name__)

@hello_api.route('/hello')
def hello():
    text = helloService.sayHello()
    return make_response(jsonify(text), 200)

#comment