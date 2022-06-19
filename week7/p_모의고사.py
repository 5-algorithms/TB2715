'''
https://programmers.co.kr/learn/courses/30/lessons/42840
'''

def solution(answers):
    answer = []

    sufo_answer = [[1, 2, 3, 4, 5],  # 5
                   [2, 1, 2, 3, 2, 4, 2, 5],  # 8
                   [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10
                   ]
    count_list = [0, 0, 0]

    for idx, x in enumerate(answers):
        len_list = [len(sufo_answer[0]), len(sufo_answer[1]), len(sufo_answer[2])]

        for sidx, sa in enumerate(sufo_answer):
            temp_idx = idx % len(sa)
            if x == sa[temp_idx]:
                count_list[sidx] += 1

    max_count = max(count_list)
    # print(max_count)
    if count_list.count(max_count) != 1:
        answer = [i + 1 for i, c in enumerate(count_list) if c == max_count]
    else:
        answer = [count_list.index(max_count) + 1]

    return answer