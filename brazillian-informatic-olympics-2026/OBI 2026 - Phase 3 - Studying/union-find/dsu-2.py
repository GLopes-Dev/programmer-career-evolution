N, M = map(int, input().split())
connections = [_ for _ in range(N+1)]
results = []
def build_road(a, b):
    way_a = find_way(a)
    way_b = find_way(b)

    if way_a != way_b:
        connections[way_a] = way_b

def find_way(x):
    if connections[x] == x:
        return x

    connections[x] = find_way(connections[x])
    return connections[x]

for _ in range(M):
    o, a, b = map(int, input().split())
    if o == 1:
        build_road(a, b)
    if o == 2:
        result1, result2 = find_way(a), find_way(b)
        results.append("YES" if result1 == result2 else "NO")

print('\n'.join(results))