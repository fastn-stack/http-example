import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return 'Web App with Python Flask!'

todo_data = [
    {
        "title": "get milk",
        "done": False
    },
    {
        "title": "cook food",
        "done": True
    }
]

@app.route('/todos/')
def todos():
    return flask.jsonify(todo_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8002)

