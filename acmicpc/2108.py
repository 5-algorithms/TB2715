'''
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.
'''
from collections import Counter
import sys

input = sys.stdin.readline
n = int(input())

array = []

for _ in range(n):
    array.append(int(input()))


print(round(sum(array)/len(array)))  # 산술평균
print(sorted(array)[len(array)//2])  # 중앙값

# 최빈값
count_dict = Counter(sorted(array))

if len(count_dict.keys()) > 1:
    temp_most_common = count_dict.most_common(2)
    print(temp_most_common[1][0]) if temp_most_common[0][1] == temp_most_common[1][1] else print(temp_most_common[0][0])
else:
    print(count_dict.most_common(1)[0][0])

# 범위
print(max(array) - min(array))