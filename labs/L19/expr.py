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

    def eval(self):
        left = self.left.eval() if isinstance(self.left, Expr) else self.left
        right = self.right.eval() if isinstance(self.right, Expr) else self.right

        if self.operator == '+':
            return left + right
        elif self.operator == '*':
            return left * right
