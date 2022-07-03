'''
https://www.acmicpc.net/problem/2110
답안 참고 -> 다시 풀어야 함
'''
import sys

input = sys.stdin.readline
n, c = map(int, input().split())

array = []
for _ in range(n):
    array.append(int(input()))

array.sort()


def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = array[0]
        count = 1

        for i in range(1, len(array)):
            if array[i] >= current + mid:
                count += 1
                current = array[i]

        if count >= c:
            global answer
            start = mid + 1
            answer = mid

        else:
            end = mid - 1

start = 1
end = array[-1] - array[0]
answer = 0

binary_search(array, start, end)
print(answer)