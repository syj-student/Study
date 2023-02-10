
def solution(n, costs):
    connect = {0}
    answer = 0
    costs.sort(key=lambda x: x[2])
    while len(connect) < n:
        for f, t, cost in costs:
            if f in connect and t in connect:
                continue
            if f in connect or t in connect:
                connect.update({f, t})
                answer += cost
                break
    return answer