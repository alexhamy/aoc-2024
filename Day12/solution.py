import sys
sys.setrecursionlimit(10000)

output = [0]

graph = []

with open("input.txt", "r") as input:
    
    for line in input:
        eq = line.strip()
        graph.append(eq)
    
    counter = {}
    
    n = len(graph)
    m = len(graph[0])
    
    seen = []
    
    def dfs(char, i, j, seen):
        if i < 0 or i >= n or j < 0 or j >= m or char != graph[i][j]:
            counter[char][1] += 1
            return
        
        if seen[i][j] == True:
            return

        seen[i][j] = True
        
        counter[char][0] += 1
        
        
        
        dfs(char, i - 1, j, seen)
        dfs(char, i, j - 1, seen)
        dfs(char, i + 1, j, seen)
        dfs(char, i, j + 1, seen)
        
    for i in range(n):
        for j in range(m):
            cur = graph[i][j]
            if cur not in counter:
                seen = [[False] * m] * n
                counter[cur] = [0,0]
                dfs(cur, i, j, seen)
    print(counter)
    
    output = 0
    
    for key in counter:
        output = counter[key][0] * counter[key][1]
    
    print(output)
                
                
                
        