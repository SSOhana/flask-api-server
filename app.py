from flask import Flask

app = Flask(__name__)

# API 가 있어야 한다!
@app.route('/', methods = ['GET'])
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run()
