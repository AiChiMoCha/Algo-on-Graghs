import os
import sys
from collections import deque

sys.setrecursionlimit(2000)


def bipartite(adj):
    #write your code here
    return -1



if __name__ == '__main__':
     # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 切换工作目录到脚本所在目录
    os.chdir(script_dir)
    
    with open('input7.txt', 'r') as file:
        input_data = file.read()
        print(input_data)
    print('-------')
    data = list(map(int, input_data.split()))
    n, m = data[0:2]
    data = data[2:]
   # undirected gragh
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b)
        adj[b - 1].append(a)
    adj_m=[[x - 1 if isinstance(x, int) and x > 0 else x for x in sublist] for sublist in adj]
    
    print(adj)
    print(adj_m)

    visited = [False]*len(adj_m)
    print(bipartite(adj))
   
    
    

