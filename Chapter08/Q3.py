n = int(input())
k = list(map(int, input().split()))

d = [0] * n
d[0] = k[0]
d[1] = max(k[0], k[1])

for i in range(2, n):
    '''R
    1. (i-1)번째 식량창고를 털기로 결정한 경우 현재의 식량창고를 털 수 없다 
    2. (i-2)번쨰 식량창고를 털기로 결정한 경우 현재의 식량창고를 털 수 있다. 
    '''
    if d[i-1] > d[i-2]:
        d[i] = d[i-1]
    else:
        d[i] = k[i] + d[i-2]

    # 한 줄로 하면
    d[i] = max(d[i-1], d[i-2] + k[i])

print(d[n-1])