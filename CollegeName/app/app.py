from CollegeName.Service.ServiceProvider import get_jokes, get_joke, add_jokes, delete_joke, update_joke
from flask import Flask, request

app = Flask(__name__)


## Joke API

@app.route("/getJokes", methods=['GET'])
def handle_get_all():
    return get_jokes()


@app.route("/getJoke", methods=['GET'])
def handle_get_one():
    return get_joke()


@app.route("/addJoke", methods=['POST'])
def handle_add_joke():
    request_data = request.json
    joke = request_data['addJoke']
    print(joke)
    return add_jokes(joke)


@app.route("/updateJokes", methods=['PUT'])
def handle_update_joke():
    request_data = request.json
    return update_joke(request_data['updateJoke'], request_data['updateJokeWith'])



