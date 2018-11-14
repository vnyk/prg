"""
Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation.
"""


#!/bin/python3

if __name__ == '__main__':
    n = int(input())
    a = bin(n)[2:].split('0')
    cnt = max(len(a[i]) for i in range(len(a)))
    print(cnt)
