class Solution:
	def convert(self, s: str, numRows: int) -> str:
		str_map = collections.defaultdict(str)
		numrows_idx = 0
		up, down = 1, -1
		for c in s:
			if numrows_idx == 0:
				move = up
			elif numrows_idx == numRows - 1:
				move = down
			str_map[numrows_idx] += c
			numrows_idx += move
		return ''.join(str_map.values())