import sys

# n = int(input())
n = int(sys.stdin.readline())

array = sorted(int(sys.stdin.readline()) for _ in range(n))

for x in array:
    print(x)

