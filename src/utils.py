from __future__ import annotations

from faker import Faker

from .models import *

fake = Faker()


def seed_human() -> Human:
    name = fake.name()
    age = fake.random_int(min=18, max=100)
    return Human(name=name, age=age).save()


def seed_business(human: Human) -> Business:
    profit = fake.random_int(min=10000, max=1000000)
    business = Business(profit=profit).save()
    human.owns.connect(business)
    business.owner.connect(human)
    return business
