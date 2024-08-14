def expandNode(graph, i, j, visited, n):

    if i < 0 or i >= n or j < 0 or j >= n or graph[i][j] == 0 or visited[i][j] == 1:
        return
    
    visited[i][j] = 1
    expandNode(graph, i+1, j, visited, n)
    expandNode(graph, i-1, j, visited, n)
    expandNode(graph, i, j+1, visited, n)
    expandNode(graph, i, j-1, visited, n)








def Count_Islands(graph, n):
    visited = [[0 for i in range(n)] for j in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and visited[i][j] == 0:
                expandNode(graph, i, j, visited, n)
                ans += 1
    return ans


def main():
    graph = [[0,0,0,0,0,1,1],[1,1,0,0,0,0,0],[1,1,0,1,0,1,1],[1,1,0,1,0,1,1],[1,1,0,0,1,0,1],[1,1,1,1,1,0,0],[0,0,0,1,1,1,1]]
    n = len(graph)
    ans = Count_Islands(graph, n)
    print("Number of islands: ",ans)

main()