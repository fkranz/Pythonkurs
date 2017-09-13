#! /usr/bin/env python3

def foo(x, y):
    global a
    a = 42
    x,y = y,x
    b = 33
    b = 17
    c = 100
    print("Inside a:", a)
    print("Inside b:", b)
    print("Inside x:", x,)
    print("Inside y:", y)

a,b,x,y = 1,15,3,4
foo(17,4)
print("Outside a:", a)
print("Outside b:", b)
print("Outside x:", x,)
print("Outside y:", y)
