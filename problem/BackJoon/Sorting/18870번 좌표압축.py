import sys

# input
n = int(sys.stdin.readline())
lstinput = list(map(int, sys.stdin.readline().split()))

# solve
lsttmp = sorted(set(lstinput))
dic = {lsttmp[i] : i for i in range(len(lsttmp))}

# pirnt
for i in lstinput:
	print(dic[i], end=' ')


## have to use dict data set (for Time complexity)