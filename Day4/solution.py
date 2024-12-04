graph = []

directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
              (1, 1), (1, -1), (-1, 1), (-1, -1)]

output = {'total':0}

with open("input.txt", "r") as input:
    
    for line in input:
        graph.append(line.strip())
    
    n = len(graph)
    m = len(graph[0])
    
    def dfs(cur, i , j, dirx, diry):
        if i < 0 or i >= n or j < 0 or j >= m or len(cur) > 5:
            return
        if cur + graph[i][j] == "XMAS":
            output['total'] += 1
            return
        dfs(cur + graph[i][j], i + dirx, j + diry, dirx, diry)
        
    def valid(i, j):
        if i-1 < 0 or i+1 >= n or j-1 < 0 or j+1 >= m:
            return
        
        check1 = graph[i-1][j-1] == 'M' and graph[i+1][j+1] == 'S' and graph[i+1][j-1] == 'S' and graph[i-1][j+1] == 'M'
        
        check2 = graph[i-1][j-1] == 'S' and graph[i+1][j+1] == 'M' and graph[i+1][j-1] == 'M' and graph[i-1][j+1] == 'S'
        
        check3 = graph[i-1][j-1] == 'M' and graph[i+1][j+1] == 'S' and graph[i+1][j-1] == 'M' and graph[i-1][j+1] == 'S'
        
        check4 = graph[i-1][j-1] == 'S' and graph[i+1][j+1] == 'M' and graph[i+1][j-1] == 'S' and graph[i-1][j+1] == 'M'
        
        if check1 or check2 or check3 or check4:
            output['total'] += 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'A':
                valid(i, j)
                
print(output)
