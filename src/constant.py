from enum import Enum

class Relation(str, Enum):
    FRIEND_WTIH = "FRIEND_WTIH"
    OWNS = "OWNS"
    OWNED_BY = "OWNED_BY"
