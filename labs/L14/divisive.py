# Check value before operation
# def fraction(a, b):
#     if b == 0:
#         return 'NaN'

#     return a / b

# Catch error
def fraction(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'NaN'
