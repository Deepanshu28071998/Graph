def buildGraph(edges, n):
    graph = [[] for i in range(n)]

    for edge in edges:
        src1 = edge[0]
        src2 = edge[1]

        des1 = edge
        des2 = edge[::-1]
        graph[src1].append(des1)
        graph[src2].append(des2)

    return graph

def hasPath(graph, n, src, des, visited):
    if src == des:
        return True
    nbrs = graph[src]

    for nbr in nbrs:
        curNbr = nbr[1]
        if visited[curNbr] == 0:
            visited[curNbr] = 1
            ans = hasPath(graph, n, curNbr, des, visited)
            if ans == True:
                return True
    return False 

def main():
    edges = [[0,1],[0,2],[1,3],[2,3],[3,4],[4,5],[4,6],[5,7],[6,7]]
    n = 8
    graph = buildGraph(edges, n)
    src = 0
    des = 7
    visited = [0 for i in range(n)]
    visited[src] = 1
    ans = hasPath(graph, n, src, des, visited)
    print(buildGraph(edges, n))
    print(hasPath(graph, n, src, des, visited))


main()