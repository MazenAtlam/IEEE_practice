#!/usr/bin/python3

def min(x, y, z):
    if x <= y and x <= z:
        return x

    if y <= x and y <= z:
        return y

    return z

n, k, l, c, d, p, nl, np = map(int, input().split(" "))
milis_of_drink = k * l / nl
lime_slices = c * d
salt = p / np
toasts = int(min(milis_of_drink, lime_slices, salt) / n)
print(toasts)
