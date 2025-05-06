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
    return wrapper ##always need to return the wrapper

def make_emphasis(func):
    def wrapper(*args, **kwargs):
        return '<em>' + func(*args, **kwargs) + '</em>'
    return wrapper

def make_underlined(func):
    def wrapper(*args, **kwargs):
        return '<u>' + func(*args, **kwargs) + '</u>'
    return wrapper

@app.route("/contact")
@make_bold
@make_underlined
def contact():
    return "Contact details!"



@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there! {name}, you are {number} years old!"
## new excercise on how to use decorators with kwargs and args
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function()
        return wrapper


@is_authenticated_decorator

def create_blog_post(user):
    print(f"This is {user.name}'s new blog post")

new_user = User("bart")
create_blog_post(new_user)


if __name__ == "__main__":
    app.run(debug=True)
