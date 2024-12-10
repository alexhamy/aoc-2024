import sys
sys.setrecursionlimit(10000)

output = [0]

graph = []

output_start = set()

order = '0123456789'

with open("input.txt", "r") as input:
    
    for line in input:
        eq = line.strip()
        graph.append(eq)
    
    max_x = len(graph[0])
    max_y = len(graph)
    
    def dfs(cur_idx, i, j, start):
        if i < 0 or i >= max_y or j < 0 or j >= max_x or cur_idx > 10 or order[cur_idx] != graph[i][j]:
            return
        if int(order[cur_idx]) == 9:
            output[0] += 1
            output_start.add((start, (i,j)))
            return
        dfs(cur_idx + 1, i + 1, j, start)
        dfs(cur_idx + 1, i, j + 1, start)
        dfs(cur_idx + 1, i - 1, j, start)
        dfs(cur_idx + 1, i, j - 1, start)
    
    for i in range(max_y):
        for j in range(max_x):
            if graph[i][j] == '0':

                dfs(0, i, j, (i, j))
    
    print(output[0])
    print(len(output_start))