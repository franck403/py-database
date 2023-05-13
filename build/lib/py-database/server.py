from flask_cors import CORS, cross_origin
from flask import Flask,request
import py-database
import asyncio
import threading
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/database/get')
def get():
    dbname = request.args.get('dbname')
    name = request.args.get('name')
    return py-database.action.get(py-database.action(dbname),name)

@app.route('/database/add')
def adddata():
    dbname = request.args.get('dbname')
    name = request.args.get('name')
    data = request.args.get('content')
    py-database.action.add(py-database.action(dbname),name,data)
    return py-database.action.get(py-database.action(dbname),name)

@app.route('/database/replace')
def replacedata():
    dbname = request.args.get('dbname')
    name = request.args.get('name')
    data = request.args.get('content')
    py-database.action.replace(py-database.action(dbname),name,data)
    return py-database.action.get(py-database.action(dbname),name)

@app.route('/database/all')
def all():
    dbname = request.args.get('dbname')
    name = request.args.get('name')
    return py-database.action.all(py-database.action(dbname),name)

@app.route('/')
def home():
    return "py-database api"

async def main():
    runner = app.run()
    asyncio.create_task(runner)

def run():
    import asyncio
    asyncio.run(main())