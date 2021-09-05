def BFS(graph, start, goal):
    if(start == goal):
        return [start]
    queue = list()
    discovered = list()
    layer = list()
    parent = list()
    path = list()
    for i in range(len(graph)):
        discovered.append(False)
        layer.append(999)
        parent.append(i)
    queue.append(start)
    discovered[start] = True
    layer[start] = 0
    while queue:
        u = queue.pop(0)
        for v in graph[u]:
            if(discovered[v] == False):
                queue.append(v)
                discovered[v] = True
                layer[v] = layer[u]+1
                parent[v] = u
                if(v == goal):
                    while(v != parent[v]):
                        path.append(v)
                        v = parent[v]
                    return path[::-1]