#!/usr/bin/python

s = 0
n = int(input("n: "))

for x in range(1, n+1):
    a = float(input("%d: "%(x)))
    s += a

print("average: %d"%(s/n))

