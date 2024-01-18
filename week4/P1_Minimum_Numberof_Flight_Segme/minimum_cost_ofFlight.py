import os
import sys
from collections import deque

sys.setrecursionlimit(2000)


def distance(adj, cost, s, t):
    #write your code here
    return -1



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
    data = data[2:-2]
   # directed gragh
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    print(data)
    print(edges)
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    
    print(adj)
    print(cost)

    s, t = data[0] - 1, data[1] - 1
   
    print(distance(adj, cost, s, t))
    
