from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def homepage():

    return """
    <h1>Hello heroku</h1>
    """

@app.route("/hello/<string:name>/")
def hello(name):
    return render_template('test.html',name = name)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

