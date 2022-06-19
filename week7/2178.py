import math
from collections import deque

n, m = map(int, input().split())
array = []

for _ in range(n):
    array.append(list(map(int, input())))

queue = deque()
queue.append((0, 0))

history = [ [math.inf] * m ] * n

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while queue:
    cx, cy = queue.popleft()

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if array[nx][ny] == 0:
            continue

        if array[nx][ny] == 1:
            array[nx][ny] = array[cx][cy] + 1
            queue.append((nx, ny))

print(array[n-1][m-1])