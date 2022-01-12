import sys
import collections

n = int(sys.stdin.readline())
tree = collections.defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

leafs = list()
for k, v in tree.items():
    if len(v) == 1:
        leafs.append(k)

answer = [0] * (n + 1)
while n >= 1:
    n -= len(leafs)
    tmp = list()
    for leaf in leafs:
        if leaf != 1:
            neighbor = tree[leaf].pop()
            answer[leaf] = neighbor
            tree[neighbor].remove(leaf)

            if len(tree[neighbor]) == 1:
                tmp.append(neighbor)

            leafs = tmp

print(*answer[2:], sep='\n')
