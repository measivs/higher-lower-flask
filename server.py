from flask import Flask
from random import randint
app = Flask(__name__)
real_number = randint(1, 9)

@app.route('/')
def first():
    return '<h1> Guess a number between 0 and 9 </h1>'\
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<int:number>')
def guess(number):
    if number < real_number:
        return '<h1 style="color: red;"> Too low, try again! </h1>'\
           '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    if number > real_number:
        return '<h1 style="color: purple;"> Too high, try again! </h1>'\
           '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">' 
    if number == real_number:
        return '<h1 style="color: green;"> You found me! </h1>'\
           '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'           


if __name__ == '__main__':
    app.run(debug=True)

