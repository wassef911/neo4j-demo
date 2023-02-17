# HOMEWORK: Neo4j Demo

a demo project to working with a graph database, mainly having two endpoint to insert and read data.

**Pip**: 22.0.4

**Python**: 3.8.16

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

---

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

in your browser check "http://localhost:5000/", and it should return totals:

```json
  total humans = 7 , total businesses = 9
```

now, doing an empty POST on "http://localhost:5000/human", should give create a new human and return it's data:

```json
  {
  uid: "93f8ed0e-af0b-11ed-96f6-d7b46fcf4698"
  name: "Ann Mcbride",
  age: 84,
  created_at: "2023-02-17T22:39:38.041960+00:00",
  friends: [ ],
  businesses: [ ],
  }
```

you can also do a GET to get a list of humans ...

doing an empty POST on "http://localhost:5000/business", should give create a new business and add a RelationshipTo the last created human...
also GET list of businesses is available.

---

and finally accesing: http://localhost:7474/browser/ should take to Neo4j's user interface.

![Screenshot](https://github.com/wassef911/neo4j-demo/blob/master/screenshot.png?raw=true)
