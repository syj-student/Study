n = int(input())
number_line = list(map(int, input().split()))
sort_line = sorted(number_line)


def check_order(n):
    for i in range(len(n) - 1):
        if n[i] < n[i+1]:
            return False
    return True


if check_order(number_line):
    print(-1)
    exit(0)

for i in range(1, n):
    right = number_line[i:]
    if check_order(right):
        left = number_line[:i]
        last = left.pop()
        right.append(last)
        right.sort()
        idx = right.index(last)
        if idx + 1 < len(right):
            left.append(right.pop(idx+1))
            left += right
        else:
            left += right
        print(*left)
        break
