import sys
input = sys.stdin.readline


def union(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return True
    if x < y:
        parents[y] = x
    else:
        parents[x] = y
    return False

def find(k):
    while k != parents[k]:
        k = parents[k]
    return k

n,m = map(int,input().split())
parents = [i for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    if union(a, b):
        print(i+1)
        break
else:
    print(0)