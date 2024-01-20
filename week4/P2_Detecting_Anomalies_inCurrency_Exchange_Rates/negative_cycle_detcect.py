import os
import sys

sys.setrecursionlimit(2000)

dist = []
visited = []

def negative_cycle(adj, cost):
    global dist
    global visited
    # Initialize distances and visited arrays
    dist = [float('inf')] * len(adj)
    visited = [0] * len(adj)

    for vertex in range(len(adj)):
        if not visited[vertex]:
            if explore(vertex, adj, cost):
                return 1
    return 0

def explore(v, adj, cost):
    global dist
    global visited
    visited[v] = 1
    for i in range(len(adj[v])):
        neighbor = adj[v][i]
        if dist[neighbor] > dist[v] + cost[v][i]:
            dist[neighbor] = dist[v] + cost[v][i]
            if explore(neighbor, adj, cost):
                return 1
    return 0

if __name__ == '__main__':
    # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 切换工作目录到脚本所在目录
    os.chdir(script_dir)

    with open('input9.txt', 'r') as file:
        input_data = file.read()
        print(input_data)
    print('-------')
    data = list(map(int, input_data.split()))
    n, m = data[0:2]
    data = data[2:-2]
    # directed graph
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)

    print(adj)
    print(cost)

    print(negative_cycle(adj, cost))
