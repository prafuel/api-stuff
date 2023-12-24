from random import randint
from flask import Flask,jsonify


def get_joke():
    with open('jokes.txt','r') as jokes_txt:
        jokes = [joke.strip() for joke in jokes_txt.readlines()]
    return jokes

jokes = get_joke()

app = Flask(__name__)
@app.route("/",methods=['get'])
def home():
    path = ['/one-liner','/get-context-joke','/get-joke-list']
    return jsonify(path)

@app.route("/one-liner",methods=['get'])
def one_liner() :
    return jokes[randint(0,len(jokes)-1)]

@app.route("/get-context-joke")
def get_context_joke():
    return "Working on... <a href='/'>Back</a>"

@app.route("/get-joke-list")
def joke_list():
    return jsonify(jokes)

if __name__ == "__main__":
    app.run(port=8000, debug=True)