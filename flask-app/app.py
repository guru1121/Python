from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return "hello flask"

@app.route('/hello', metods= ["GET", "POST"])
def hello():
    if request.method == "GET":
        return "Get request"
    if request.method == "Post":
        return "Post request"
        

if __name__ == "__main__":
    app.run(debug=True)