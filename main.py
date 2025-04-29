from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

## this is one way of adding decorators using html syntax
# can use this solution https://stackoverflow.com/questions/70676351/is-there-a-flask-function-called-make-bold-i-am-very-confused-as-i-am-not-abl
@app.route("/bye")
def bye():
    return "<u><em><b>Bye!</b></em></u>"

## this is one way of adding decorators

def make_bold(func):
    def wrapper(*args, **kwargs):
        return '<b>' + func(*args, **kwargs) + '</b>'
    return wrapper

def make_emphasis(func):
    def wrapper(*args, **kwargs):
        return '<em>' +func(*args, **kwargs) + '</em>'

def make_underlined(func):
    def wrapper(*args, **kwargs):
        return '<u>' +func(*args, **kwargs) + '</u>'

@app.route("/byebye")
@make_bold
@make_emphasis
@make_underlined

def bye():
    return "ByeBye!"



@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there! {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)
