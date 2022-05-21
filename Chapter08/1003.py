t = int(input())

test_case_array = [int(input()) for _ in range(t)]

fibo_array = []
fibo_array.append({0: 1, 1:0})
fibo_array.append({0: 0, 1:1})

for test_case in test_case_array:
    for i in range(len(fibo_array), test_case+1):
        fibo_array.append({
            0: fibo_array[i-1][0] + fibo_array[i-2][0],
            1: fibo_array[i-1][1] + fibo_array[i-2][1]
        })


for test_case in test_case_array:
    print(f'{fibo_array[test_case][0]} {fibo_array[test_case][1]}')