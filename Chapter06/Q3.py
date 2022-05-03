N = int(input())

s_list = []
for _ in range(N):
    name, score = input().split()
    s_list.append((name, int(score)))

sorted_s_list = sorted(s_list, key=lambda x: x[1])

for name, score in sorted_s_list:
    print(name, end=' ')