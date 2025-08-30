#!/usr/bin/env python3

def print_fibonacci(n):
    if n == 0:
        print([])
        return
    
    fib = [0, 1]
    
    if n == 1:
        print([0])
        return
    
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    
    print(fib[:n])
