import os

def number_of_components(adj):
    result = 0
    visited = [False for x in range(len(adj))]

    def dfs(v):
        visited[v-1] = True
        for neighbor in adj[v-1]:
            if not visited[neighbor-1]: #recreation break out at the youngest offspring
                dfs(neighbor)


    for vertex in range(len(adj)):
        if visited[vertex] is False:
            result += 1
            dfs(vertex)

    return result

if __name__ == '__main__':
     # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 切换工作目录到脚本所在目录
    os.chdir(script_dir)
    
    with open('input2.txt', 'r') as file:
        input_data = file.read()
        print(input_data)
    print('-------')
    data = list(map(int, input_data.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges: #by adjacent metrics def
        adj[a-1].append(b)
        adj[b-1].append(a)  
    visited = [False] * len(adj)
    print(number_of_components(adj))
