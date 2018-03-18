from flask import Flask
from flask import request


app = Flask(__name__)


@app.before_request
def print_header():
    print(request.headers)


@app.route('/')
def hello():
    return 'world'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
