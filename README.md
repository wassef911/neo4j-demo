# HOMEWORK: Neo4j Demo

a demo project to working with a graph database, mainly having two endpoint to insert and read data.

```sh
├── README.md
├── docker-compose.yml
├── main.py (server proc)
├── neo4j
|  ├── data
|  ├── import
|  ├── logs
|  └── plugins
├── requirements.txt
└── venv
```

## Getting Started

Pip: 22.0.4
Python: 3.8.16

copy the **.env-example** to file called **.env**

install dependencies via (please use a venv):

```sh
pip install -r requirements.txt
```

start the database:

```sh
docker-compose up -d
```

start the project:

```sh
flask --app main.py --debug run
```

in your browser check "http://localhost:5000/", and it should insert dummy data to your database.

now, checking "http://localhost:5000/data", should give you a list of the data:

```json
[
  {
    "age": 30,
    "name": "Monji"
  },
  {
    "age": 44,
    "name": "Mohsen"
  },
  {
    "age": 44,
    "name": "Jhony"
  }
]

and finally accesing: http://localhost:7474/browser/ should take to Neo4j's user interface.

## TODO add img
```
