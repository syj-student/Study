import collections

def solution(bridge_length, weight, truck_weights):
	answer = 0
	bridge = collections.deque([0]*bridge_length)
	acc = 0
	i = 0
	while acc or i != len(truck_weights):
		answer += 1
		acc -= bridge.popleft()
		if i < len(truck_weights) and acc + truck_weights[i] <= weight:
			bridge.append(truck_weights[i])
			acc += truck_weights[i]
			i += 1
		else:
			bridge.append(0)
	return answer

a = solution(2, 10, [7, 4, 5, 6])
print(a)