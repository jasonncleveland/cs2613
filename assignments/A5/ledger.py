from scanner import Scanner
from type_ import Type


ACCOUNTS = {}

ACTION_OPEN = [Type.OPEN, Type.IDENT, Type.CURRENCY]
ACTION_TRANSFER = [Type.TRANSFER, Type.IDENT, Type.IDENT, Type.CURRENCY]
ACTION_BALANCE = [Type.BALANCE, Type.IDENT]


def add_balances(l_balance: int, r_balance: int) -> int:
    """adds two floating point numbers stored in integer format"""
    left = float("{0}.{1}".format(str(l_balance)[:-2], str(l_balance)[-2:]))
    right = float("{0}.{1}".format(str(r_balance)[:-2], str(r_balance)[-2:]))
    return float(''.join("{0:.2f}".format(left + right).split('.')))


def open_account(account_name: str, starting_balance: int):
    """opens a new account with the specified starting balance"""
    ACCOUNTS[account_name] = starting_balance


def transfer_balance(from_account: str, to_account: str, balance: int):
    """removes desired funds from first account and adds them to second"""
    ACCOUNTS[from_account] = add_balances(ACCOUNTS[from_account], balance * -1)
    ACCOUNTS[to_account] = add_balances(ACCOUNTS[to_account], balance)


def account_balance(account_name: str) -> tuple:
    """returns a tuple of the account name and current balance"""
    return (account_name, ACCOUNTS.get(account_name, 0))


def ledger(input: str):
    """manages ledger actions passed in via a newline separated string"""
    actions = [list(Scanner(line)) for line in input.strip().splitlines()]

    for action in actions:
        action_type = [token.type for token in action]
        if action_type == ACTION_OPEN:
            open_account(action[1].value, action[2].value)
        elif action_type == ACTION_TRANSFER:
            transfer_balance(action[1].value, action[2].value, action[3].value)
        elif action_type == ACTION_BALANCE:
            yield account_balance(action[1].value)
