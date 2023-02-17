from flask import Flask, jsonify
from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

user = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')
db_host = os.environ.get('DB_HOST',default='localhost')
db_port = os.environ.get('DB_PORT',default=7687)

driver = GraphDatabase.driver(f'bolt://{db_host}:{db_port}', auth=(user, password))

@app.route('/data')
def get_data():
    with driver.session() as session:
        result = session.run('MATCH (n) RETURN n')
        data = [dict(record['n']) for record in result]
        return jsonify(data)

@app.route('/')
def index():
    with driver.session() as session:
        session.run("CREATE (:Person {name: 'Monji', age: 30})")
        session.run("CREATE (:Person {name: 'Mohsen', age: 44})")
        session.run("CREATE (:Person {name: 'Jhony', age: 44 })")
        return 'Data inserted'

if __name__ == '__main__':
    app.run()
