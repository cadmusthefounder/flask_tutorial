from flask import Flask
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

@app.route('/hello')
def hello():
	return 'Hello from the other side.'

if __name__ ==  '__main__':
	app.run(host='127.0.0.1', port=8080)