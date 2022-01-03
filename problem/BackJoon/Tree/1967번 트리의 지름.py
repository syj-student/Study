import sys
import heapq
import collections


# make graph
n = int(sys.stdin.readline())
graph = collections.defaultdict(list)
while True:
    try:
        depart, dst, cost = map(int, sys.stdin.readline().split())
        graph[depart].append((dst, cost))
        graph[dst].append((depart, cost))
    except:
        break


# calculate distance
def dijkstra(start, cnt):
