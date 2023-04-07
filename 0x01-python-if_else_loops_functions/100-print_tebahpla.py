#!/usr/bin/python3
for d in range(ord('z'), ord('a') - 1, -1):
    print("{:d}".format((d - (ord('a') - ord('A'))) if d % 2 else d), end='')
