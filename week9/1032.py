n = int(input())

array = []
for _ in range(n):
    array.append(input())

if n == 1:
    print(array[0])

else:
    arr_len = len(array[0])

    answer = []
    for idx in range(arr_len):
        ta = array[0][idx]

        for a_arr in array[1:]:
            if a_arr[idx] != ta:
                ta = '?'
                break
        answer.append(ta)

    print(''.join(answer))