from flask import Flask, jsonify, request
from flask_cors import CORS 
from database import Database

app = Flask(__name__)
CORS(app)
db = Database('lamb.db')

@app.route('/hello')
def hello():
	return 'hello from the other side.'

@app.route('/lambs', methods=['POST'])
def create_lamb():
    params = get_request_params()
    with db:
        lamb = db.create_lamb(**params)
        db.commit()
        response = {
            'id': lamb.id,
            'name': lamb.name,
            'weight': lamb.weight,
            'dietary_type': lamb.dietary_type
        }
        return jsonify(response)

@app.route('/lambs/<id>', methods=['GET','PUT','DELETE'])
def get_put_delete_lamb(id):
    with db:
        if request.method  == 'GET':
            lamb = db.get_lamb(id)
        elif request.method == 'PUT':
            params = get_request_params()
            lamb = db.update_lamb(id, **params)
            db.commit()
        elif request.method == 'DELETE':
            lamb = db.delete_lamb(id)
            db.commit()

        response = {
            'id': lamb.id,
            'name': lamb.name,
            'weight': lamb.weight,
            'dietary_type': lamb.dietary_type
        }
        return jsonify(response)

def get_request_params():
    params = request.get_json()
    if not params:
        params = request.form.to_dict()

    query_params = {k: v for k, v in request.args.items()}
    params = {**params, **query_params}
    return params


if __name__ ==  '__main__':
	app.run(host='127.0.0.1', port=8080, threaded=True)