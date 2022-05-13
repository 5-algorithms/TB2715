''''
정수 X가 주어질 때 연산 4개를 적절히 사용해서 1을 만들기.
연산을 사용하는 횟수의 최솟값 출력

case 1. / 5
case 2. /3
case 3. /2
case 4. -1

'''

x = int(input())
d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i-1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)

    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)

    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)


print(d[x])