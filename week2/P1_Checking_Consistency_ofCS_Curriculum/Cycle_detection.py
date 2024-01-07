import os


visited = []
recStack = []

def isCyclicUtil(adj, v):
    global visited
    global recStack
    if not visited[v]:
        visited[v] = True
        recStack[v] = True
        for w in adj[v]:
            if (not visited[w]) and isCyclicUtil(adj, w):
                return True
            elif recStack[w]:
                return True
    recStack[v] = False
    return False

def acyclic(adj):
    global visited
    global recStack

    visited = [False] * len(adj)
    recStack = [False] * len(adj)
    
    for v in range(len(adj)):
        if isCyclicUtil(adj, v):
            return 1 #True
    
    return 0

if __name__ == '__main__':
     # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 切换工作目录到脚本所在目录
    os.chdir(script_dir)
    
    with open('input3.txt', 'r') as file:
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
    print(acyclic(adj))
