class Expr:
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def __eq__(self, other):
        return (
            self.operator == other.operator
            and self.left == other.left
            and self.right == other.right
        )
