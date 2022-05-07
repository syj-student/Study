import collections


def solution(q1, q2):
	if not q1 or not q2:
		return 0
	q1 = collections.deque(q1)
	q2 = collections.deque(q2)
	answer = 0
	lim_q1 = len(q1) + len(q2)
	lim_q2 = len(q1) + len(q2)
	sum_q1 = sum(q1)
	sum_q2 = sum(q2)
	while True:
		if sum_q1 == sum_q2:
			return answer
		if lim_q1 == 0 or lim_q2 == 0:
			return -1
		if sum_q1 > sum_q2:
			p = q1.popleft()
			q2.append(p)
			sum_q1 -= p
			sum_q2 += p
			lim_q1 -= 1
			answer += 1
		if sum_q1 < sum_q2:
			p = q2.popleft()
			q1.append(p)
			sum_q2 -= p
			sum_q1 += p
			lim_q2 -= 1
			answer += 1