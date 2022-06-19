"""
https://programmers.co.kr/learn/courses/30/lessons/77484
"""


def solution(lottos, win_nums):
    answer = []

    num_of_zero = lottos.count(0)

    correct_count = 0
    for x in win_nums:
        if x in lottos:
            correct_count += 1

    min = 7 - correct_count if correct_count > 1 else 6

    tcc = correct_count + num_of_zero
    max = 7 - tcc if tcc > 1 else 6

    answer = [max, min]

    return answer