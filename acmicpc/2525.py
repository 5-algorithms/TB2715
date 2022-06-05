cur_hour, cur_minute = map(int, input().split())

total_minute = int(input())

cost_hour = total_minute//60
cost_minute = total_minute - (cost_hour*60)

pr_m = (cur_minute + cost_minute) % 60
cur_hour += (cur_minute + cost_minute) // 60

pr_h = (cur_hour + cost_hour) % 24

print(f'{pr_h} {pr_m}')