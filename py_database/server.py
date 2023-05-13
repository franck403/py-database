from flask_cors import CORS, cross_origin
from flask import Flask,request
import py_database
import asyncio
import threading
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/database/get')
def get():
    dbname = request.args.get('dbname')
    name = request.args.get('name')
    return py_database.action.get(py_database.action(dbname),name)

@app.route('/database/add')
def adddata():
    dbname = request.args.get('dbname')
    name = request.args.get('name')
    data = request.args.get('content')
    py_database.action.add(py_database.action(dbname),name,data)
    return py_database.action.get(py_database.action(dbname),name)

@app.route('/database/replace')
def replacedata():
    dbname = request.args.get('dbname')
    name = request.args.get('name')
    data = request.args.get('content')
    py_database.action.replace(py_database.action(dbname),name,data)
    return py_database.action.get(py_database.action(dbname),name)

@app.route('/database/all')
def all():
    dbname = request.args.get('dbname')
    name = request.args.get('name')
    return py_database.action.all(py_database.action(dbname),name)

@app.route('/')
def home():
    return "py_database api"

async def main():
    runner = app.run()
    asyncio.create_task(runner)

def run():
    import asyncio
    asyncio.run(main())