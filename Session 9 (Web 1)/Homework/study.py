from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/about-me')
def dmd():
    post = {
        'name': 'Dao Duc',
        'age' : 18,
        'work': 'Student',
        'school': 'Rmit University',
        'hobbies': 'Football, Gaming',
    }
    return render_template('index2.html', post = post)


@app.route('/school')
def school():
    return redirect("http://techkids.vn/")

if __name__ == '__main__':
  app.run(debug=True)
