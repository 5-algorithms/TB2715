'''
n개의 정수로 이루어진 임의의 수열이 주어진다. 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다. 단, 수는 한 개 이상 선택해야 한다.
예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자. 여기서 정답은 12+21인 33이 정답이 된다.
'''

n = int(input())
array = list(map(int, input().split()))

sum = [array[0]]

for idx in range(len(array) - 1):
    sum.append(max(sum[idx] + array[idx+1], array[idx+1]))
    # sum[idx]와 array[i+1] 인덱스의 숫자를 합한 값과 array[i+1] 숫자를 비교하여 더 큰 숫자를 sum 리스트에 추가
    # 이전 값이랑 더해서 크면 더하고, 안크면 그냥 유지

print(max(sum))