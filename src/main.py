from flask import Flask, jsonify, request, make_response
from faker import Faker
from neomodel import config

from .models import *
from .db import get_db_url
from faker import Faker


app = Flask(__name__)

fake = Faker()
config.DATABASE_URL = get_db_url()


@app.route("/human", methods=["GET", "POST"])
def humans():
    if request.method == "GET":
        humans = Human.nodes.all()
        return make_response(jsonify([h.to_json() for h in humans]), 200)
    if request.method == "POST":
        name = fake.name()
        age = fake.random_int(min=18, max=100)
        human = Human(name=name, age=age).save()
        return make_response(jsonify(human.to_json()), 201)


@app.route("/business", methods=["GET", "POST"])
def business():
    if request.method == "GET":
        businesses = Business.nodes.all()
        return make_response(jsonify([b.to_json() for b in businesses]), 200)
    if request.method == "POST":
        profit = fake.random_int(min=10000, max=1000000)
        business = Business(profit=profit).save()

        human = Human.nodes.order_by("-created_at").first()

        human.owns.connect(business)
        business.owner.connect(human)
        return make_response(jsonify(business.to_json()), 201)


@app.route("/")
def index():
    return make_response(
        f"total humans = {Human().nodes.all().__len__()} , total businesses = {Business().nodes.all().__len__()}",
        200,
    )


if __name__ == "__main__":
    app.run()
