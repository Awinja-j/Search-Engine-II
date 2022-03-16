from flask import Flask
from flask_mongoengine import MongoEngine

import logging

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'your_database',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()