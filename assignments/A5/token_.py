from type_ import Type

class Token:
    def __init__(self, type: Type, value: any):
        self.type = type
        self.value = value
    
    def __str__(self):
        if self.type == Type.CURRENCY:
            dollars = str(self.value)[:-2]
            cents = str(self.value)[-2:]
            return '[{}: {}.{}]'.format(self.type.name, dollars, cents)        
        else:
            return '[{}: {}]'.format(self.type.name, self.value)

    def __eq__(self, other):
        l_value = self.value.lower() if isinstance(self.value, str) else self.value
        r_value = other.value.lower() if isinstance(other.value, str) else other.value
        return (
            self.type == other.type
            and l_value == r_value
        )
