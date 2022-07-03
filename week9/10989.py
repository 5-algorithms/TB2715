'''
https://www.acmicpc.net/problem/10989
'''

import sys
input = sys.stdin.readline

n = int(input())
array = [0] * 10001

for _ in range(n):
    x = int(input())
    array[x] += 1

for x in range(len(array)):
    if array[x] != 0:
        for y in range(array[x]):
            print(x)