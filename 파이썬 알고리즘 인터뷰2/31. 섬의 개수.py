# https://leetcode.com/problems/number-of-islands/

class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		islandCnt = 0
		dx = [1, -1, 0, 0]
		dy = [0, 0, 1, -1]
		for row in range(len(grid)):
			for col in range(len(grid[0])):
				if grid[row][col] == "1":
					stack = list()
					stack.append((row, col))
					while stack:
						tmp = stack.pop()
						grid[tmp[0]][tmp[1]] = -1
						for i in range(4):
							nx = tmp[0] + dx[i]
							ny = tmp[1] + dy[i]
							if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == "1":
								stack.append((nx, ny))
					islandCnt += 1
		return islandCnt