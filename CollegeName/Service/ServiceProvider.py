import random

from CollegeName.helper.HelperClass import list_of_jokes as jokes


# This will Handle the CRUD APP working

# C = Create
# R = Read
# U = Update
# D = Delete

## use case for : our M L model
## NLP - NLTK Basic model

### TODO Day2


# get multiple Jokes
def get_jokes():
    return jokes


# get a joke
def get_joke():
    return random.choice(jokes)


# add a joke
def add_jokes(joke):
    jokes.append(joke)
    print(jokes)
    return f'joke has been added to the database new joke = {jokes[len(jokes) - 1]}'


# update a joke
def update_joke(joke_to_be_updated, updated_joke):
    for idx, item in enumerate(jokes):
        if joke_to_be_updated == item:
            jokes[idx] = updated_joke
    return get_jokes()


# delete a joke
def delete_joke(joke):
    previous_count = len(jokes)
    jokes.remove(joke)
    print(jokes)
    return f'joke has been removed from the database old count = {previous_count} new count = {len(jokes)} '
