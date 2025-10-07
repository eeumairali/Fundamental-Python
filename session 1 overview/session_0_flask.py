import flask

app = flask.Flask(__name__)

@app.route('/')
def home():
    name = "umair"
    return flask.render_template('index.html',content=name)

@app.route('/about')
def about():
    return "<h1>About Page</h1>"


if __name__ == '__main__':
    app.run(debug=True)