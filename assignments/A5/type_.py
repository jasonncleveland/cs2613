from enum import Enum

class Type(Enum):
    BALANCE = 0
    CURRENCY = 1
    IDENT = 2
    OPEN = 3
    TRANSFER = 4

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.value == other.value
        )
