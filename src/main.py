from __future__ import annotations

from faker import Faker
from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request
from neomodel import config

from .db import get_db_url
from .models import *
from .utils import *

app = Flask(__name__)
fake = Faker()
config.DATABASE_URL = get_db_url()


@app.route('/human', methods=['GET', 'POST'])
def humans():
    if request.method == 'GET':
        return make_response(jsonify([h.to_json() for h in Human.nodes.all()]), 200)
    if request.method == 'POST':
        human = seed_human()
        return make_response(jsonify(human.to_json()), 201)


@app.route('/human/make_friendship', methods=['GET'])
def make_friendship():
    new_human = Human.nodes.order_by('-created_at').first()
    old_human = Human.nodes.order_by('created_at').first()
    new_human.friends_with.connect(old_human)
    return make_response(jsonify(new_human.to_json()), 201)


@app.route('/business', methods=['GET', 'POST'])
def business():
    if request.method == 'GET':
        businesses = Business.nodes.all()
        return make_response(jsonify([b.to_json() for b in businesses]), 200)
    if request.method == 'POST':
        human = Human.nodes.order_by('-created_at').first()
        business = seed_business(human)
        return make_response(jsonify(business.to_json()), 201)


@app.route('/')
def index():
    open_up_shop = fake.random_int(min=5, max=10)
    [seed_business(seed_human()) for i in range(open_up_shop)]
    return make_response(
        {
            'total_humans': Human().nodes.all().__len__(),
            'total_businesses': Business().nodes.all().__len__(),
            'new_opportunities': open_up_shop,
        },
        201,
    )


if __name__ == '__main__':
    app.run()
