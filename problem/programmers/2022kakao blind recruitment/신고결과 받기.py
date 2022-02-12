def solution(id_list, report, k):
    answer = []
    d = dict()
    bad_user = set()
    for user in id_list:
        d[user] = [set(), 0]
    for l in report:
        a, b = l.split()
        if b not in d[a][0]:
            d[a][0].add(b)
            d[b][1] += 1
            if d[b][1] >= k:
                bad_user.add(b)
    for report_users, cnt in d.values():
        answer.append(len(report_users & bad_user))
    return answer
