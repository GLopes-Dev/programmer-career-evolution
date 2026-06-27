import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())
connections = defaultdict(set)

for p in range(M):
    A1, A2 = map(str, sys.stdin.readline().split())
    connections[A1].add(A2)
    connections[A2].add(A1)

sorted_people = sorted(connections.keys())
for a in sorted_people:
    print(f'{a}: {sorted(*connections[a])}')