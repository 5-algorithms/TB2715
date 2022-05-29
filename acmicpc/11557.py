t = int(input())

for _ in range(t):
    n = int(input())

    h_name = ''
    h_count = -1
    for _ in range(n):
        name, count = input().split()
        if h_count < int(count):
            h_name = name
            h_count = int(count)

    print(h_name)