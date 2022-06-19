'''
https://programmers.co.kr/learn/courses/30/lessons/72410
'''

import re


def solution(new_id: str):
    answer = ''

    temp_id = new_id

    temp_id = temp_id.lower()  # step 1
    temp_id = re.sub('([^a-z0-9-_.])', '', temp_id)  # step 2
    while '..' in temp_id:
        temp_id = temp_id.replace('..', '.')  # step 3

    # step 4
    if len(temp_id) > 0 and temp_id[0] == '.':
        temp_id = temp_id[1:]
    if len(temp_id) > 0 and temp_id[-1] == '.':
        temp_id = temp_id[:-1]

    # step 5
    if temp_id == '':
        temp_id = 'a'

    # step 6
    if len(temp_id) >= 16:
        temp_id = temp_id[:15]

        if temp_id[-1] == '.':
            temp_id = temp_id[:-1]

    # step 7
    if len(temp_id) <= 2:
        while len(temp_id) < 3:
            temp_id += temp_id[-1]

    answer = temp_id
    return answer


solution("=.=")