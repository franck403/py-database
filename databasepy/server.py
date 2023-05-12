from flask_cors import CORS, cross_origin
from flask import Flask,request
import databasepy
import asyncio
import threading
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/dataqbase/get')
def get():
    dbname = request.args.get('dbname')
    name = request.args.get('name')
    return databasepy.action.get(databasepy.action(dbname),name)

@app.route('/')
def home():
    return "py-database api"

async def main():
    runner = app.run()
    asyncio.create_task(runner)

def run():
    import asyncio
    asyncio.run(main())