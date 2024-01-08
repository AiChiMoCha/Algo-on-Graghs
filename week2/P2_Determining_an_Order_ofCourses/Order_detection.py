import os

visited = []
order = []

def explore(adj, v, visited):
    global order
    visited[v] = True
    for neighbor in adj[v]:
        if not visited[neighbor]:
            explore(adj, neighbor, visited)
    order.insert(0, v)

    

def toposort(adj):
    global visited
    global order
    visited = [False] * len(adj)
    for v in range(len(adj)):
        if not visited[v]:
            explore(adj, v,visited)
    return order


if __name__ == '__main__':
     # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 切换工作目录到脚本所在目录
    os.chdir(script_dir)
    
    with open('input4.txt', 'r') as file:
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
    visited = [False] * len(adj)
    order = toposort(adj_m)
    for x in order:
        print(x + 1, end=' ')
