def solution(numbers):
    answer = set()

    for i in range(len(numbers) - 1):
        target_num = numbers[i]
        for j in range(i+1, len(numbers)):
            answer.add(numbers[j] + target_num)

    answer = sorted(list(answer))
    return answer

print(solution([2, 1, 3, 4, 1]))
