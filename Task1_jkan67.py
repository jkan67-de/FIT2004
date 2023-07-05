from min_heap import *

def dijsktra(graph, initial,final):
    Discovered=MinHeap(6105)
    Finalised=[]
    Vert_parent=[-1]*6105
    Discovered.insert((initial,0))

    while Discovered.currentSize>0:
        current=Discovered.delMin()
        for i in range(len(graph[current[0]])):
            connected_node=graph[current[0]][i]
            if Discovered.vertices[connected_node[0]]==-2:
                Discovered.insert((connected_node[0],connected_node[1]+current[1]))
                Vert_parent[connected_node[0]]= current[0]

            elif Discovered.vertices[connected_node[0]]!=-1 and Discovered.heapList[Discovered.vertices[connected_node[0]]][1]>connected_node[1]+current[1]:
                Discovered.replace(Discovered.vertices[connected_node[0]],(connected_node[0],connected_node[1]+current[1]))
                Vert_parent[connected_node[1]]= current[0]

        Finalised.append(current)
        Discovered.vertices[current[0]] = -1
        if current[0]==final:
            break

    if initial==final:
        path=str(initial)
        dist = Finalised[-1][1]
    else:
        path=str(Finalised[-1][0])
        node=Vert_parent[Finalised[-1][0]]
        while Vert_parent[node]!=-1:
            path= str(node)+' --> '+path
            node=Vert_parent[node]
        path=str(initial)+' --> '+path
        dist=Finalised[-1][1]

    return path,dist

def create_graph(edges_doc):
    Graph = []
    for i in range(6105):
        Graph.append([])

    for edge in edges_doc:
        a = edge.split(' ')
        for i in range(3):
            a[i] = int(a[i])
        Graph[a[0]].append((a[1],a[2]))
        Graph[a[1]].append((a[0],a[2]))
    return Graph

def print_task1(info):
    print('Shortest Path and Distance: ')
    print(info[0])
    print('Total route distance: ' + str(info[1]) + '\n')

E = open('edges.txt')
Graph=create_graph(E)


