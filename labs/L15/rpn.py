#!/usr/bin/python3

import sys

stack = []

def process(line):
    if line in ['+', '-', '*', '/', '^', 'swap']:
        b = stack.pop()
        a = stack.pop()

    if line == '+':
        stack.append(a + b)
    elif line == '-':
        stack.append(a - b)
    elif line == '*':
        stack.append(a * b)
    elif line == '/':
        stack.append(a // b)
    elif line == '^':
        stack.append(a ** b)
    elif line == 'clear':
        stack.clear()
    elif line == 'dup':
        stack.append(stack[-1])
    elif line == 'pop':
        stack.pop()
    elif line == 'swap':
        stack.append(b)
        stack.append(a)
    elif line == 'print':
        return int(stack[-1])
    else:
        stack.append(int(line))

def process_list(lines):
    out = []
    for line in lines:
        if line == 'quit':
            return out
        result = process(line)
        if result is not None:
            out.append(result)
    return out        
