from collections import Counter

user_input = list(map(int, input().split()))

count_result = Counter(user_input)

if len(count_result.keys()) == 3:
    print(max(user_input) * 100)

elif len(count_result.keys()) == 2:
    for key, value in count_result.items():
        if value == 2:
            print(1000 + key*100)

else:
    print(10000 + user_input[0]*1000)