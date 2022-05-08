def binary_search(array, target, start, end):
    if start >= end:
        return None 
    
    mid = (start + end)//2
    # if array[mid] == target:
    #     return mid
    # elif array[mid] > target:
    #     return binary_search(array, target, start, mid-1)
    # else:
    #     return binary_search(array, target, mid+1, end)
    total_list = list(x - mid for x in array)
    total_list = list(0 if x < 0 else x for x in total_list)
    total = sum(total_list)
    
    if total == target:
        return mid
    elif target < total:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)
    

N, M = map(int, input().split())

len_list = list(map(int, input().split()))
sorted(len_list)

# print(binary_search(len_list, M, 0, max(len_list)))

'''
Answer
이 문제와 같은 파라메트릭 서치 문제 유형은 이진 탐색을 재귀적으로 구현하지 않고 반복문을 이용해 구현하면 더 간결하게 문제를 풀 수 있다. 
'''

start = 0
end = max(len_list)

result = 0
while(start <= end):
    total = 0
    mid = (start+end) // 2
    for x in len_list:
        if x > mid:
            total += x-mid

    if total < M:
        end = mid-1

    else:
        result = mid
        start = mid + 1

print(result)
