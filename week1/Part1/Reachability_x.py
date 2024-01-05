
def reach(adj, x, y):
    visited = [False] * len(adj)
    explore(adj, x, visited)
    return visited[y-1]

def explore(adj, v, visited):
    print('v'+ str(v))
    visited[v-1] = True
    for neighbor in adj[v-1]:
        print('n'+ str(neighbor))
        print(visited)
        print(not visited[neighbor-1])
        if not visited[neighbor-1]: #recreation break out at the youngest offspring
            print('next')
            explore(adj, neighbor, visited)

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input_data = file.read()
        print(input_data)
    print('-------')
    data = list(map(int, input_data.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x = 1
    y = n
    #print(y)
    adj = [[] for _ in range(n)]
    for (a, b) in edges: #by adjacent metrics def
        adj[a-1].append(b)
        adj[b-1].append(a)  
    visited = [False] * len(adj)
    print(visited)
    print(adj)
    explore(adj,x,visited)
    result = reach(adj, x, y)
    print('reachability:' + str(result))
