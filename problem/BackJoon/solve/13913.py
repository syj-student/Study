import heapq

a, b = map(int, input().split())
stack = [(0, a, [a])]
answer = (float('inf'), )
while stack:
    step, now, his = heapq.heappop(stack)
    if step >= answer[0]:
        continue
    if now == b:
        if step < answer[0]:
            answer = (step, his)
        break
    if step + 1 < answer[0]:
        heapq.heappush(stack, (step + 1, now-1, his + [now-1]))
        heapq.heappush(stack, (step + 1, now+1, his + [now+1]))
        heapq.heappush(stack, (step + 1, now*2, his + [now*2]))
print(answer[0])
print(*answer[1])

# a, b = map(int, input().split())
# dp = [False] * (b + 1)
