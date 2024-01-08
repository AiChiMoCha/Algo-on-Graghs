import os
import sys

sys.setrecursionlimit(2000)

visited = []
order = []

def reverseGraph(adj):
    n = len(adj)
    adjr = [[] for _ in range(n)]
    for v in range(len(adj)):
        for w in adj[v]:
            adjr[w].append(v)
    return adjr

def explore(adj, v):
    global visited
    visited[v] = True
    for w in adj[v]:
        if not visited[w]:
            explore(adj, w)

def exploreForOrder(adj, v):
    global visited
    global order
    visited[v] = True
    for w in adj[v]:
        if not visited[w]:
            exploreForOrder(adj, w)
    order.insert(0, v)

def toposort(adj):
    global visited
    global order
    visited = [False] * len(adj)
    for v in range(len(adj)):
        if not visited[v]:
            exploreForOrder(adj, v)
    return order

def number_of_strongly_connected_components(adj):
    global visited
    result = 0
    adjr = reverseGraph(adj)
    order = toposort(adjr)
    visited = [False] * len(adj)
    for v in order:
        if not visited[v]:
            explore(adj, v)
            result += 1
    return result


if __name__ == '__main__':
     # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 切换工作目录到脚本所在目录
    os.chdir(script_dir)
    
    with open('input5.txt', 'r') as file:
        input_data = file.read()
        print(input_data)
    print('-------')
    data = list(map(int, input_data.split()))
    n, m = data[0:2]
    data = data[2:]
   # 在有向图中，只有一个方向的边
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b)

    print(adj)
    adj_m=[[x - 1 if isinstance(x, int) and x > 0 else x for x in sublist] for sublist in adj]
    
    print(adj_m)
    print(number_of_strongly_connected_components(adj_m))

