'''
2차원 평면 위의 점 N개가 주어진다.
좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
'''

n = int(input())
axis_list = []

for _ in range(n):
    axis_list.append(list(map(int, input().split())))

axis_list.sort(key=lambda x: (x[0], x[1]))
for item in axis_list:
    print(f'{item[0]} {item[1]}')