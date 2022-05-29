t = int(input())

for _ in range(t):
    count = [0, 0]
    for _ in range(9):
        y_count, k_count = map(int, input().split())

        count[0] += y_count
        count[1] += k_count

    if count[0] > count[1]:
        print('Yonsei')
    elif count[0] == count[1]:
        print('Draw')
    else:
        print('Korea')