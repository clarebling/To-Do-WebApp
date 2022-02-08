from flask import Flask, request
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
# db = SQL


@app.route('/') 
def index():
    return 'Hello!'

@app.route('/todo/<id>', methods=['DELETE'])
def delete_todo(id):
    if request.method == 'DELETE':
        print('DELETING ', id)
        return {}


@app.route('/todo', methods=['POST'])
def add_todo():
    if request.method == 'POST':
        print(Frequency = request.json['Frequency'], Title = request.json['Title'])
        return {}

@app.route('/todos', methods=['GET', 'PUT'])
def todos():
    if request.method == 'GET':
        return {
            "tasks": [
                {
                    "Frequency": "Daily",
                    "Title": "Feed David",
                },
                {
                    "Frequency": "Weekly",
                    "Title": "Do Laundry"
                },
            ],
            "counts": 2
        }

if __name__=="__main__":
    app.run(debug=True)
