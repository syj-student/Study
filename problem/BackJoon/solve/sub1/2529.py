import itertools
import sys

n = int(sys.stdin.readline())
num = [str(i) for i in range(10)]
es = sys.stdin.readline().strip().split()


def checker(acc):
    if eval(acc):
        return True
    return False


def dfs(n, nums, acc='', depth=0, answer=''):
    if n == depth:
        print(answer)
        return True
    for i in range(10):
        if nums[i] not in acc:
            if not acc:
                new_acc = nums[i]
            else:
                new_acc = acc + es[depth-1] + nums[i]
                if not eval(new_acc):
                    continue
            if dfs(n, nums, new_acc, depth + 1, answer + nums[i]):
                return True


dfs(n+1, list(reversed(num)))
dfs(n+1, num)
