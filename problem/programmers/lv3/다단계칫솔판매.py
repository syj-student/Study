from collections import defaultdict

def solution(enroll, referral, seller, amount):
    answer = defaultdict(int)
    m = dict()
    for idx in range(len(referral)):
        m[enroll[idx]] = referral[idx]

    def work(worker, income):
        nonlocal answer, m
        if income == 0:
            return
        if worker in m:
            commission = income // 10
            answer[worker] += income - commission
            work(m[worker], commission)
        else:
            answer[worker] += income

    for s, e in zip(seller, amount):
        work(s, e*100)
    ret = [0] * len(enroll)
    for i, worker in enumerate(enroll):
        ret[i] = answer[worker]
    return ret

print(solution(
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["young", "john", "tod", "emily", "mary"],
    [12, 4, 2, 5, 10]
))