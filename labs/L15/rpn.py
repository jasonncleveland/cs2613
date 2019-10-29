#!/usr/bin/python3

import sys

stack = []

def process(line):
    if line in ['+', '-', '*', '/']:
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
    elif line == 'clear':
        stack.clear()
    else:
        stack.append(int(line))
