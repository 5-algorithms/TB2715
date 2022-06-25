'''
https://www.acmicpc.net/problem/1038
풀이: https://velog.io/@imnotmoon/Python-%EB%B0%B1%EC%A4%80-1038.-%EA%B0%90%EC%86%8C%ED%95%98%EB%8A%94-%EC%88%98
'''

from collections import deque
N = int(input())  # 몇번째 감소하는 수를 얻을 것인가
q = deque([])

for x in range(10):
    q.append(str(x))

total = len(q)-1
if N <= 9:
    print(q[N])
    exit(0)

while q:
    c = q.popleft()
    for i in range(10):
        if int(c[-1]) <= i:
            break
        else:
            q.append(c + str(i))
            total += 1
            if total == N:
                print(q[-1])
                exit(0)

print(-1)