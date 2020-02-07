from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

app.config['TESTING'] = True
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

from app import views

if __name__ == '__main__':
    app.run()
