import re

from token_ import Token
from type_ import Type

class Scanner:

    _word_pattern = re.compile(r'(\w+)', re.IGNORECASE)
    _currency_pattern = re.compile(r'([-]?(\d+)(\.(\d+))?)')

    def __init__(self, input_string: str):
        self.tokens_string = input_string
        self.token_strings = self.parse_tokens_string(self.tokens_string)

    def __next__(self):
        if len(self.token_strings) > 0:
            return self.parse_token(self.token_strings.pop(0))
        else:
            raise StopIteration
    
    def __iter__(self):
        self.token_strings = self.parse_tokens_string(self.tokens_string)
        return self

    def parse_token(self, token: str) -> Token:
        """converts a string token into the appropriate Token object"""
        if self._currency_pattern.match(token):
            match = self._currency_pattern.match(token).group(1)
            dollars, cents = "{0:.2f}".format(float(match)).split('.')
            return Token(Type.CURRENCY, int("{0}{1}".format(dollars, cents)))
        elif self._word_pattern.match(token):
            match = self._word_pattern.match(token).group(1)
            return Token(Type.get_type_by_name(match), match)
        else:
            raise ValueError(token)
    
    def parse_tokens_string(self, tokens_string: str) -> list:
        """splits the incoming string at any whitespace"""
        return re.split(r'\s+', tokens_string.strip())
