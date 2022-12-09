# def solution(n, costs):
#     answer = 0
#     costs.sort(key = lambda x: x[2]) # 비용기준으로 오름차순 정렬
#     connect = set([costs[0][0]]) # 연결을 확인하는 집합
    
#     # Kruskal 알고리즘으로 최소 비용 구하기
#     while len(connect) != n:
#         for cost in costs:
#             if cost[0] in connect and cost[1] in connect:
#                 continue
#             if cost[0] in connect or cost[1] in connect:
#                 connect.update([cost[0], cost[1]])
#                 answer += cost[2]
#                 break
                
#     return answer

# print(solution(
#     4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
# ))
from collections import defaultdict

def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    connection = set([costs[0][0]])
    answer = 0
    while len(connection) != n:
        for cost in costs:
            if cost[0] in connection and cost[1] in connection:
                continue
            if cost[0] in connection or cost[1] in connection:
                connection.update([cost[0], cost[1]])
                answer += cost[2]
                break
    return answer