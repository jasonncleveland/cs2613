import re

class Ages:

    _pattern = re.compile(r'(\w+) is (\d+)', re.IGNORECASE)

    def __init__(self, input_):
        self._input = input_
        self.age_list = self.parse_input(self._input)
    
    def __next__(self):
        # Return values until the list is empty
        if self.age_list:
            age = self.age_list[0]
            self.age_list = self.age_list[1:]
            # Convert to correct data types before returning
            return (str(age[0]), int(age[1]))
        else:
            raise StopIteration
    
    def __iter__(self):
        self.age_list = self.parse_input(self._input)
        return self
    
    def parse_input(self, input_):
        matches = self._pattern.findall(input_)
        # Filter out any matches that aren't capitalized
        return [match for match in matches if match and match[0][0].isupper()]
