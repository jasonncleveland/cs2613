def make_counter(x):
    print('entering make_counter')
    while True:
        yield x
        print('incrementing x')
        x = x + 1

def make_counter2(x):
    count = x
    def counter():
        nonlocal count
        retval = count
        count += 1
        return retval

    return counter

print('first')
counter = make_counter(100)
print('second')
print(next(counter))
print('third')
print(next(counter))
print('last')