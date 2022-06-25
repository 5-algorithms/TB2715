def solution(nums):
    answer = 0

    available_count = len(nums)//2
    temp_nums = set(nums)

    if len(temp_nums) <= available_count:
        return len(temp_nums)
    else:
        return available_count