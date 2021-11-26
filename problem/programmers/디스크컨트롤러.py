import heapq

def solution(jobs):
	jobs.sort(reverse=True)
	total_work_amount = len(jobs)
	total_work_time = 0
	acc_work_time = 0
	heap = list()
	while heap or jobs:
		while jobs and jobs[-1][0] <= acc_work_time:
			request_time, work_time = jobs.pop()
			heapq.heappush(heap, (work_time, request_time))

		if not heap:
			acc_work_time = jobs[-1][0]
			continue

		handle_work_time, handle_request_time = heapq.heappop(heap)
		acc_work_time += handle_work_time
		total_work_time += acc_work_time - handle_request_time
	return total_work_time // total_work_amount