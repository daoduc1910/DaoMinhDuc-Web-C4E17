from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    posts = [
    {
        "title": "Thơ con cóc",
        "content": "Watermelon",
        "author": "Tuấn Anh",
        "gender": 1
    },
    {
        "title": "Thơ trà sữa",
        "content": "Strawberry",
        "author": "Thu Thảo",
        "gender": 0
    }

    ]
    return render_template("index.html", posts = posts)


@app.route('/c4e')
def sayhi():
    return "Hi C4E 17"

@app.route('/say-hello/<name>/<age>')
def sayhello(name, age):
    return "Hi {0}, you are {1} years old".format(name, age)

@app.route('/sum/<int:a>/<int:b>')

def sum(a, b):
    return "{0} + {1} = {2}".format(a, b, (a+b))

if __name__ == '__main__':
  app.run(debug=True) #khởi động sever
