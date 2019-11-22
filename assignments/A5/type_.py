from enum import Enum

class Type(Enum):
    BALANCE = 0
    CURRENCY = 1
    IDENT = 2
    OPEN = 3
    TRANSFER = 4

    def __eq__(self, other):
        """determine if two Type objects have the same attributes"""
        return (
            self.name == other.name
            and self.value == other.value
        )

    @staticmethod
    def get_type_by_name(name):
        """returns type object based on given name. IDENT if none found"""
        for member in Type:
            if member.name.lower() == name.lower():
                return member
        return Type.IDENT
