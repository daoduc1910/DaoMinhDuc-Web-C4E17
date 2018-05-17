from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def user(username):
    user_info = {
        'Duc': {
            "name": "Dao Minh Duc",
            "age" : 18,
            "gender": 1,
            "work": "Student"
        },
        'Minh': {
            "name": "Minh Minh",
            "age" : 33,
            "gender": 2,
            "work": "Student"
        },
        'phananh': {
            "name": "Nguyen Phan Anh",
            "age" : 23,
            "gender": 1,
            "work": "Student"
        },
        'don': {
            "name": "Phạm Quý Đôn",
            "age" : 22,
            "gender": 1,
            "work":"Techkids"
        }
    }

    if username in user_info.keys():
        user = user_info[username]
        return render_template('index3.html', user = user)
    else:
        return "User infomation not found"


if __name__ == '__main__':
  app.run(debug=True)
