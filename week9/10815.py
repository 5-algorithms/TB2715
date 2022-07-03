'''
https://www.acmicpc.net/problem/10815
'''

n = int(input())
n_array = list(map(int, input().split()))

m = int(input())
m_array = list(map(int, input().split()))

n_array.sort()


def binary_search(array, start, end, target):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    return None

for i in range(m):
    if binary_search(n_array, 0, n-1, m_array[i]) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')