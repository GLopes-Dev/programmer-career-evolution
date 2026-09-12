N, M = map(int, input().split())
connections = [_ for _ in range(N+1)]
results = []

def build_road(a, b):
    way_a = find_way(a)
    way_b = find_way(b)
    if way_a == way_b:
        return "CYCLE"
    else:
        connections[way_a] = way_b
        return "OK"

def find_way(x):
    if connections[x] == x:
        return x

    connections[x] = find_way(connections[x])
    return connections[x]

for _ in range(M):
    a, b = map(int, input().split())
    result = build_road(a, b)
    results.append(result)

print('\n'.join(results))
