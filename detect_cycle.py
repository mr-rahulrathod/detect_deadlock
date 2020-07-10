from collections import deque

def addEdge(adj: list, u, v):
    adj[u].append(v)
    adj[v].append(u)

def isCyclicConnected(adj: list, s, V,visited: list):
    parent = [-1] * V
    q = deque()
    visited[s] = True
    q.append(s)

    while q != []:
        u = q.pop()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
                parent[v] = u
            elif parent[u] != v:
                return True
    return False

def isCyclicDisconnected(adj: list, V):

    # Mark all the vertices as not visited
    visited = [False] * V

    for i in range(V):
        if not visited[i] and \
               isCyclicConnected(adj, i, V, visited):
            return True
    return False
