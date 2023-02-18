# HOMEWORK: Neo4j Demo

a demo project to working with a graph database, mainly having two endpoint to insert and read data.

### requirements:

**Pip**: 22.0.4

**Python**: 3.8.16

---

```sh
├── README.md
├── docker-compose.yml
├── requirements.txt
├── screenshot.png
├── src
|  ├── __init__.py
|  ├── constant.py
|  ├── db.py
|  ├── main.py
|  └── models.py
└── venv
```

---

## Getting Started

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
flask --app src/main.py --debug run
```

in your browser check "http://localhost:5000/",

and it will run a seed script and return totals:

```json
{
  "total_businesses": 25,
  "total_humans": 25,
  "new_opportunities": 5 # total number new random human/business
}
```

### Human

now, doing an empty POST on "http://localhost:5000/human",

should create a new human and return it's data:

```json
{
    "uid": "0a788d76-af8a-11ed-b23b-45cbc219d73c",
    "name": "Sean Novak",
    "age": 90,
    "businesses": [
      {
        "uid": "0a788d76-af8a-11ed-b23b-45cbc219d73c",
        "created_at": "2023-02-18T13:44:53.437408+00:00",
        "profit": 848288
      }
    ],
    "created_at": "2023-02-18T13:44:53.437408+00:00"
  },
```

you can also do a GET to get a list of all humans...

doing a GET on "http://localhost:5000/human/make_friendship",

should create a **FRIEND_WTIH** relation between (first/last) humans:

```json
{
  "name": "Vanessa Rodriguez",
  "uid": "bfa37f9e-af8a-11ed-b23b-45cbc219d73c",
  "age": 60,
  "businesses": [
    {
      "created_at": "2023-02-18T13:49:57.386466+00:00",
      "profit": 588887,
      "uid": "bfa37f9e-af8a-11ed-b23b-45cbc219d73c"
    },
    {
      "created_at": "2023-02-18T13:49:57.386466+00:00",
      "profit": 118838,
      "uid": "bfa37f9e-af8a-11ed-b23b-45cbc219d73c"
    }
  ],
  "created_at": "2023-02-18T13:49:57.386466+00:00"
}
```

---

### Business

doing an empty POST on "http://localhost:5000/business",

should create a new business **OWNED_BY** the last created human...

```json
{
  "created_at": "2023-02-18T13:44:53.437408+00:00",
  "profit": 848288,
  "uid": "0a788d76-af8a-11ed-b23b-45cbc219d73c"
}
```

you can also do a GET to get a list of all businesses...

---

and finally accessing: http://localhost:7474/browser/

should take to Neo4j's user interface.

![Screenshot](https://github.com/wassef911/neo4j-demo/blob/master/screenshot.png?raw=true)
