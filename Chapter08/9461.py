# 0 1 2 3 4 5 6 7 8 9 10 11
# 1 2 3 4 5 6 7 8 9 10 11 12
# 1 1 1 2 2 3 4 5 7 9 12 16
# 0 0 0 1 0 1 1 1 2 2 3 4


test_case_count = int(input())
array = [1, 1, 1]

for _ in range(test_case_count):
    n = int(input())

    for idx in range(len(array), n):
        array.append(array[idx-3] + array[idx-2])

    print(array[n-1])