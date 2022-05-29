'''
수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.
'''
import sys

n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
sum_array = [0 for _ in range(n+2)]
sum_array[1] = array[0]

for idx, x in enumerate(array[1:]):
    sum_array[idx+2] = sum_array[idx+1] + x

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(sum_array[j] - sum_array[i - 1])
