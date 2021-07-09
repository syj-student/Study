from collections import deque
import sys

input = sys.stdin.readline

###
## solve
###

# parsing (make graph)
y, x = map(int, input().strip().split())
graph = [list(map(int, input().strip())) for _ in range(y)]

# BFS
print(graph)