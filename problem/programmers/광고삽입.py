import bisect
import datetime
import re
def solution(play_time, adv_time, logs):
	if play_time == adv_time:
		return "00:00:00"
	play_time = convertStringtoIntTime(play_time)
	adv_time = convertStringtoIntTime(adv_time)
	int_logs = list()
	for log in logs:
		log1, log2 = map(convertStringtoIntTime ,log.split('-'))
		int_logs.append((log1, log2))

	# timeline
	max_time = 0
	for ad_start in range(int_logs[0][0], play_time - adv_time + 1):
		ad_end = ad_start + adv_time
		acc = 0
		for start, end in int_logs:
			if ad_start <= start <= ad_end:
				if end <= ad_end:
					acc += end - start
				else:
					acc += ad_end - start
		max_time = max(max_time, acc)
	return convertInttoStringTime(max_time)



def convertStringtoIntTime(string_time):
	string_time = list(map(int, string_time.split(':')))
	int_time = string_time[0]*3600 + string_time[1]*60 + string_time[2]
	return int_time

def convertInttoStringTime(int_time):
	h, remainder = divmod(int_time, 3600)
	m, s = divmod(remainder, 60)
	string_time = str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(s).zfill(2)
	return string_time



a = solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])
print(a)