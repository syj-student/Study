import sys
sys.setrecursionlimit(10 ** 9)

def decoder(start, end):
	if start > end:
		return
	global data
	root = data[start]
	idx = start + 1
	while idx <= end:
		if root < data[idx]:
			break
		idx += 1
	decoder(start + 1, idx - 1)
	decoder(idx, end)
	print(root)

data = list()
while True:
	try:
		data.append(int(sys.stdin.readline()))
	except:
		break
lg = len(data)
decoder(0, lg - 1)