import sys

sys.stdin.readline()
lst = list(map(int, sys.stdin.readline().split()))


# min check
def check_order(l):
    for i in range(1, len(l)):
        if l[i-1] > l[i]:
            return False
    return True


for i in range(len(lst)):
    right = lst[i:]
    if check_order(right):
        if i == 0:
            print(-1)
            break
        answer = lst[:i-1]
        tmp = sorted(lst[i-1:], reverse=True)
        idx = tmp.index(lst[i-1])
        if idx + 1 < len(tmp):
            answer.append(tmp.pop(idx+1))
            answer += tmp
        else:
            answer += tmp
        print(*answer)
        break
