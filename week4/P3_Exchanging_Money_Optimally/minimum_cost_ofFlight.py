import os
import sys


sys.setrecursionlimit(2000)

dist = []
visited = []

def Dijkstra(v,adj,cost):
    #Dijkstra's Algo

    global dist,visited
    visited[v] = True

    for neighbor in adj[v]:

        if dist[neighbor] > dist[v] + cost[v][adj[v].index(neighbor)]:
            dist[neighbor] = dist[v] + cost[v][adj[v].index(neighbor)]
  
        #ongoing
    for neighbor in adj[v]:
        if not visited[neighbor] and neighbor == min(adj[v], key=lambda x: cost[v][adj[v].index(x)]):
            Dijkstra(neighbor,adj,cost)



def distance(adj, cost, s, t):
    global dist, visited
    dist = [float('inf')] * len(adj)
    visited = [False] * len(adj)
    dist[s] = 0
    Dijkstra(s, adj, cost)

    return dist[t] if dist[t] != float('inf') else -1




if __name__ == '__main__':
     # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 切换工作目录到脚本所在目录
    os.chdir(script_dir)
    
    with open('input8.txt', 'r') as file:
        input_data = file.read()
        print(input_data)
    print('-------')
    data = list(map(int, input_data.split()))
    n, m = data[0:2]
    s, t = data[-2] - 1, data[-1] - 1
    data = data[2:-2]
   # directed gragh
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    
    print(adj)
    print(cost)
    
    print(s,t)
   
    print(distance(adj, cost, s, t))
