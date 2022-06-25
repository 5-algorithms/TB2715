def solution(id_list, report, k):
    answer = []

    reported_dict = {}
    reporter_dict = {}
    for a_id in id_list:
        reported_dict[a_id] = set()
        reporter_dict[a_id] = set()
        
    blocked_member = set()

    for a_r in report:
        reporter, reported = a_r.split(' ')
        reported_dict[reported].add(reporter)
        reporter_dict[reporter].add(reported)
        
        if len(reported_dict[reported]) >= k:
            blocked_member.add(reported)

    for k in id_list:
        answer.append(len(blocked_member & reporter_dict[k]))

    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))