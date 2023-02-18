from __future__ import annotations

import datetime
import uuid

from neomodel import DateTimeProperty
from neomodel import IntegerProperty
from neomodel import RelationshipFrom
from neomodel import RelationshipTo
from neomodel import StringProperty
from neomodel import StructuredNode

from .constant import Relation


class BaseNode(StructuredNode):
    uid = StringProperty(unique_index=True, default=uuid.uuid1())
    created_at = DateTimeProperty(default=datetime.datetime.now())

    def to_json(self):
        return {'uid': self.uid, 'created_at': self.created_at.isoformat()}


class Business(BaseNode):
    profit = IntegerProperty(default=0)
    owner = RelationshipFrom('Human', Relation.OWNED_BY.value)

    def to_json(self):
        json_data = super().to_json()
        json_data.update(
            {
                'profit': self.profit,
            }
        )
        return json_data


class Human(BaseNode):
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=18)
    owns = RelationshipTo(Business, Relation.OWNS.value)
    friends_with = RelationshipTo('Human', Relation.FRIEND_WTIH.value)

    def to_json(self):
        json_data = super().to_json()
        json_data.update(
            {
                'name': self.name,
                'age': self.age,
                'businesses': [b.to_json() for b in self.owns.all()],
            }
        )
        return json_data
