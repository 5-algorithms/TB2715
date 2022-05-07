import sys


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            end = mid - 1

        elif array[mid] < target:
            start = mid + 1

    return None


N = int(input())
n_list = list(map(int, (sys.stdin.readline().rstrip()).split()))

M = int(input())
m_list = list(map(int, (sys.stdin.readline().rstrip()).split()))

for item in m_list:
    result = 'yes' if binary_search(n_list, item, 0, N-1) is not None else 'no'
    print(result, end=' ')