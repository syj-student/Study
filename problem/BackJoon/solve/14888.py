import sys
import itertools

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
ops = list(map(int, sys.stdin.readline().split()))
max_num = float('-inf')
min_num = float('inf')


def cal(tmp, i, depth):
    if i == 0:
        tmp += nums[depth]
    elif i == 1:
        tmp -= nums[depth]
    elif i == 2:
        tmp *= nums[depth]
    elif i == 3:
        if tmp < 0:
            tmp = -tmp // nums[depth]
            tmp *= -1
        else:
            tmp //= nums[depth]
    return tmp


def dfs(now=nums[0], depth=1):
    global max_num
    global min_num
    if depth == n:
        max_num = max(max_num, now)
        min_num = min(min_num, now)
        return
    for i in range(4):
        if ops[i]:
            ops[i] -= 1
            dfs(cal(now, i, depth), depth + 1)
            ops[i] += 1


dfs()
# new_ops = ['+'] * ops[0] + ['-'] * ops[1] + ['*'] * ops[2] + ['/'] * ops[3]
# cases = itertools.permutations(new_ops, n-1)
# tmp = [0] * ((n - 1) * 2 + 1)
# for i, j in zip(range(0, len(tmp), 2), range(0, n)):
#     tmp[i] = nums[j]
# for case in cases:
#     for i, j in zip(range(1, len(tmp), 2), range(0, n)):
#         tmp[i] = case[j]
#     out = eval(''.join(tmp))
#     max_num = max(max_num, out)
#     min_num = min(min_num, out)
print(max_num)
print(min_num)
