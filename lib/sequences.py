#!/usr/bin/env python3

def print_fibonacci(length):
    a,b=0,1
    fib_list=[]
    while len(fib_list) <length:
        fib_list.append(a)
        a, b = b, a + b
    print(fib_list)

    