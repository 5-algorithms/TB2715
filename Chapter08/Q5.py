n, m = map(int, input().split())

money_values = []
for i in range(n):
    money_values.append(int(input()))

count_list = [10001 for i in range(m + 1)]
count_list[0] = 0

for money_value in money_values:
    for idx in range(money_value, m + 1):
        # print(f'idx: {idx - money_value} \t d[idx]: {count_list[idx - money_value]}')
        if count_list[idx - money_value] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
            count_list[idx] = min(count_list[idx], count_list[idx - money_value] + 1)
            # print(count_list)

print(-1) if count_list[m] == 10001 else print(count_list[m])
 