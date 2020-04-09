#!/usr/bin/python

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

n = int(input("fibonacci number? "))
s = fibo(n)
for i in range(1, n-1):
    print("%d "%fibo(i),end="")
print("%d "%fibo(n))

print("F%d = "%n,end=""); print("%d"%fibo(n));

