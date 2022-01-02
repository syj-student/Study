import sys
import collections

# parse
a, b = map(int, sys.stdin.readline().split())
pop_list = list(map(int, sys.stdin.readline().split()))
pop_list.reverse()

# make deque
dq = collections.deque()
for i in range(1, a + 1):
    dq.append(i)

# calculate
answer = 0
while pop_list:
    pop_num = pop_list.pop()
    location = dq.index(pop_num)
    left, right = len(dq) - location, location
    if left > right:
        answer += right
        dq.rotate(-right)
        dq.popleft()
    else:
        answer += left
        dq.rotate(left)
        dq.popleft()
print(dq)
print(answer)

