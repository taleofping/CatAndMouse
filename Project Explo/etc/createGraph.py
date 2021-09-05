mapp = ['000000000000000000',
        '0000P......0..0000',
        '000000.000.0.00000',
        '0000....0.....0000',
        '0000.00...000.0000',
        '0000.0..0..0..0000',
        '0000.....0...00000',
        '0000..0....0..0000',
        '0000.00...00..0000',
        '0000....0..A.00000',
        '0000.0..00...G0000',
        '000000000000000000']

graph = list()
node = 0
for i in range(len(mapp)):
    for j in range(len(mapp[0])):
        graph.append(list())
        if(mapp[i][j] != '0'):
            if(j-1 >= 0):
                if(mapp[i][j-1] != '0'):
                    graph[node].append(node-1)
            if(j+1 <= 17):
                if(mapp[i][j+1] != '0'):
                    graph[node].append(node+1)
            if(i-1 >= 0):
                if(mapp[i-1][j] != '0'):
                    graph[node].append(node-len(mapp[0]))
            if(i+1 <= 17):
                if(mapp[i+1][j] != '0'):
                    graph[node].append(node+len(mapp[0]))
        node += 1

for a in range(len(graph)):
    print('node', a, 'is ', end='')
    for b in graph[a]:
        print(b,' ', end='')
    print('')


def BFS(graph, start, goal):
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
                    print("IS GOAL !!!")
                    print('Path is : ', end='')
                    while(v != parent[v]):
                        path.append(v)
                        v = parent[v]
                    print(path[::-1])
                    return

BFS(graph, 22, 63)




          