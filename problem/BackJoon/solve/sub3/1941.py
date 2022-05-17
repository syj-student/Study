import sys
from pprint import pprint

input = sys.stdin.readline

class_room = list()
for _ in range(5):
	class_room.append(list(input()))
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
answer = set()
checked = set()


def dfs(now, y=0, s=0, dep=0):
	global answer
	if y > 3:
		return
	tmp = tuple(sorted(now))
	if tmp in checked:
		return
	checked.add(tmp)
	if dep == 6: 
		now.sort()
		answer.add(tuple(now))
		return
	for k in range(len(now)):
		for i in range(4):
			nx = dx[i] + now[k][0]
			ny = dy[i] + now[k][1]
			if 0 <= nx < 5 and 0 <= ny < 5 and not (nx, ny) in now:
				if class_room[nx][ny] == 'Y':
					dfs(now+[(nx, ny)], y+1, s, dep+1)
				else:
					dfs(now+[(nx, ny)], y, s+1, dep+1)

for i in range(5):
	for j in range(5):
		if class_room[i][j] == 'Y':
			dfs([(i, j)], y=1)
		else:
			dfs([(i, j)], s=1)
print(len(answer))