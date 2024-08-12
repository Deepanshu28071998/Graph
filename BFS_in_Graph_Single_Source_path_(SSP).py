#from collection import deque

def buildGraph(edges,n):
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


def bfs(graph,src,visited,queue):
    while len(queue) > 0:
        removedElement = queue.pop(0)
        currentDestination = removedElement[0]
        psf = removedElement[1]
        visited[currentDestination] = 1
        print(str(currentDestination)+"|"+psf)
        nbrs = graph[currentDestination]
        for i in range(len(nbrs)):
            if nbrs[i] == 1 and visited[i] == 0:
                queue.append([i,psf+"->"+str(i)])





def main():
    n = 8
    edges = [[0,1],[0,2],[1,3],[2,3],[3,4],[4,5],[4,6],[5,7],[6,7]]

    graph = buildGraph(edges,n)

    queue = [[0,"0"]]
    visited = [0 for i in range(n)]
    src = 0
    bfs(graph,src,visited,queue)

main()