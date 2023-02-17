from flask import Flask, jsonify
from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

user = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')

driver = GraphDatabase.driver('bolt://localhost:7687', auth=(user, password))

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
        session.run("CREATE (:Person {name: 'Jhony', age: })")
        return 'Data inserted'

if __name__ == '__main__':
    app.run()
