import re

from token_ import Token
from type_ import Type

class Scanner:
    def __init__(self, input_string: str):
        self.tokens_string = input_string
        self.token_lines = self.tokens_string.splitlines()
        self.parsed_tokens = self.parse_token_lines()

    def __next__(self):
        if len(self.parsed_tokens) > 0:
            return self.parsed_tokens.pop(0)
        else:
            raise StopIteration
    
    def __iter__(self):
        self.parsed_tokens = self.parse_token_lines()
        return self
    
    def parse_token_lines(self) -> list:
        pattern = re.compile(r'\w+', re.IGNORECASE)
        results = re.findall(pattern, self.tokens_string)
        return [Token(Type.get_type_by_name(token), token) for token in results]
