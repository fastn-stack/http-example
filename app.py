import flask
from flask import redirect

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


@app.route('/add-todo/', methods=['POST'])
def add_todo():
    todo_data.append({"title": "TODO", "done": True})
    return redirect("/") 


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8002)

