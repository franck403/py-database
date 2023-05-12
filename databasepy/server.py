from flask_cors import CORS, cross_origin
from flask import Flask,request
import databasepy
import asyncio
import threading
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/database/get')
def get():
    dbname = request.args.get('dbname')
    name = request.args.get('name')
    return databasepy.action.get(databasepy.action(dbname),name)

@app.route('/database/add')
def adddata():
    dbname = request.args.get('dbname')
    name = request.args.get('name')
    data = request.args.get('content')
    databasepy.action.add(databasepy.action(dbname),name,data)
    return databasepy.action.get(databasepy.action(dbname),name)

@app.route('/database/replace')
def replacedata():
    dbname = request.args.get('dbname')
    name = request.args.get('name')
    data = request.args.get('content')
    databasepy.action.replace(databasepy.action(dbname),name,data)
    return databasepy.action.get(databasepy.action(dbname),name)

@app.route('/database/all')
def all():
    dbname = request.args.get('dbname')
    name = request.args.get('name')
    return databasepy.action.all(databasepy.action(dbname),name)

@app.route('/')
def home():
    return "py-database api"

async def main():
    runner = app.run()
    asyncio.create_task(runner)

def run():
    import asyncio
    asyncio.run(main())