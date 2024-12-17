import sys
sys.setrecursionlimit(10000)

output = []

minimum_score = [float('inf')]

vis = {}

graph = []

tracker = {}

directions = [(0,1),(1,0), (0,-1), (-1,0)]

with open("input.txt", "r") as input:
    
    for line in input:
        eq = line.strip()
        graph.append(eq)
    
    
    def astar(score, x, y, dir, visited):
        if graph[y][x] == '#':
            return
        
        visited.add((x,y))
        
        if graph[y][x] == 'E':
            if score < minimum_score[0]:
                minimum_score[0] = score
                vis[score] = visited
            elif score == minimum_score[0]:
                vis[score] = vis[score] | visited
            return
        
        if (x, y) not in tracker:
            temp = {}
            temp[dir] = score
            tracker[(x,y)] = temp
        else:
            if dir in tracker[(x,y)]:
                if tracker[(x,y)][dir] >= score:
                    tracker[(x,y)][dir] = score
                else:
                    return
            else:
                tracker[(x,y)][dir] = score
                
        if score > minimum_score[0]:
            return
        
        cur_dir = directions[dir]

        astar(score + 1, x + cur_dir[0], y + cur_dir[1], dir, visited.copy())
        astar(score + 1000, x, y, (dir - 1 + 4) % 4, visited.copy())
        astar(score + 1000, x, y, (dir + 1) % 4, visited.copy())
    
    
    cur_pos = None
    
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 'S':
                cur_pos = (i, j)
                break
    
    astar(0, cur_pos[1], cur_pos[0], 1, set())
    
    
print(minimum_score)

temp = float('inf')

for key in vis:
    temp = min(temp, key)
                
for key in vis:

    if key == temp:
        print(len(vis[key]))