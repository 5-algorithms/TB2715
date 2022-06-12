'''
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
https://www.acmicpc.net/problem/1181
'''

n = int(input())
len_dict = {}

for _ in range(n):
    user_input = input()
    if len(user_input) not in len_dict:
        len_dict[len(user_input)] = [user_input]
    else:
        len_dict[len(user_input)].append(user_input)


for k in sorted(list(len_dict.keys())):
    temp = sorted(list(set(len_dict[k])))
    list(map(print, temp))