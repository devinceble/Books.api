from flask import Flask
from flask import jsonify
from flask import Response
from flask import request
from pymongo import MongoClient
from bson.json_util import dumps
app = Flask(__name__)

client = MongoClient("mongodb://127.0.0.1:27017")
db = client.books

@app.route('/')
def main():
    return 'Books.api'

@app.route('/Books', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        books = db.books.find()
        resp = dumps(books)
        return Response(resp, status=200, mimetype='application/json')
    else:
        req = request.get_json()
        db.books.insert_one({
            'ID': req['ID'],
            'Title': req['Title'],
            'Description': req['Description'],
            'PageCount': req['PageCount']
        })
        return jsonify(req)


@app.route('/Books/<int:id>', methods=['PUT', 'DELETE'])
def book_updel(id):
    if request.method == 'PUT':
        req = request.get_json()
        db.books.update_one({ 'ID': id }, {
         '$set': {
                'ID': req['ID'],
                'Title': req['Title'],
                'Description': req['Description'],
                'PageCount': req['PageCount']
            }
        })
        return jsonify(req)
    else:
        db.books.delete_one({ 'ID': id })
        return 'Book %s Deleted' % id
