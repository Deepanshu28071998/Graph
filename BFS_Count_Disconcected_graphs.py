#def bfs(graph,src,visited,queue):


#def isCycle(graph,n):


def buildGraph(edges, n):
    graph = [[0 for i in range(n)] for j in range(n)]

    for edge in edges:
        src = edge[0]
        des = edge[1]
        graph[src][des] = 1
        graph[des][src] = 1
    return graph

def printGraph(graph):
    for row in graph:
        for e in row:
            print(e,end=" ")
        print()





def expandNode(graph,n,src,curComponent,visited):
    nbrs = graph[src]
    for i in range(len(nbrs)):
        if nbrs[i] == 1 and visited[i] == 0:
            visited[i] = 1
            curComponent.append(i)
            expandNode(graph, n, i, curComponent, visited)




def getAllComponents(graph, n):
    visited = [0 for i in range(n)]
    ans = []
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            curComponent = [i]
            expandNode(graph, n, i, curComponent, visited)
            ans.append(curComponent)
    return ans




def main():
    edges = [[0,2],[0,3],[1,3],[4,5],[6,7],[6,8],[8,9],[10,11]]
    n = 12
    graph = buildGraph(edges, n)
    queue = [[0,"0"]]
    visited = [0 for i in range(n)]
    src = 0
    ans = getAllComponents(graph,n)
    print(ans)



main()