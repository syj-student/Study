import collections
import bisect

class node():
	def __init__ (self):
		self.score = list()
		self.next_node = collections.defaultdict(node)

def solution(info, query):
	def insert(root, cand, score):
		for c in cand:
			root = root.next_node[c]
		root.score.append(score)
		# idx = bisect.bisect_left(root.score, score)
		# if idx == -1:
		# 	root.score.append(score)
		# else:
		# 	root.score.insert(idx, score)

		
	def getcnt(root, cand, score, i=0):
		if i == len(cand):
			root.score.sort()
			num = bisect.bisect_left(root.score, score)
			if num != -1:
				return len(root.score) - num
			return 0
		cnt = 0
		if cand[i] == '-':
			for c in root.next_node.keys():
				cnt += getcnt(root.next_node[c], cand, score, i+1)
		else:
			cnt = getcnt(root.next_node[cand[i]], cand, score, i+1)
		return cnt
		
		
	trie = node()
	for cand in info:
		p = cand.split()
		score = int(p.pop())
		insert(trie, p, score)

	result = list()
	for qu in query:
		tmp = qu.replace(' and', '').split()
		score = int(tmp.pop())
		p = getcnt(trie, tmp, score)
		result.append(p)

	return result