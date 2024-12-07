import sys
sys.setrecursionlimit(10000)

output = [0]
graph = []
guard_dir_char  = ('<', '^', '>', 'v')
guard_dir = [(0,-1),(-1,0),(0,1),(1,0)]
cur_dir = ''
positions = set()

with open("input.txt", "r") as input:
    
    for line in input:
        temp = line.strip()
        graph.append(temp)

    guard_x = 0
    
    guard_y = 0
    
    max_x = len(graph)
    max_y = len(graph[0])
    
    for i in range(max_x):
        for j in range(max_y):
            if graph[i][j] in guard_dir_char:
                guard_x = i
                guard_y = j
                cur_dir = graph[i][j]
                break
    
    def get_dir_char(dir):
        for i in range(4):
            if guard_dir_char[i] == dir:
                return i
    
    def search(cur_x, cur_y, dir_x, dir_y, dir_num, paths):
        if cur_x < 0 or cur_x >= max_x or cur_y < 0 or cur_y >= max_y:
            return

        if graph[cur_x][cur_y] == '#':
            cur_dir_num = (dir_num + 1) % 4
            temp1, temp2 = guard_dir[cur_dir_num]
            
            search(cur_x - dir_x, cur_y - dir_y, temp1, temp2, cur_dir_num, paths)
        else:
            positions.add((cur_x, cur_y))
            
            if (cur_x, cur_y) in paths:
                
                if dir_num in paths[(cur_x, cur_y)]:
                    output[0] += 1
                    print(1)
                    return
                
                paths[(cur_x, cur_y)].add(dir_num)
                
            else:
                paths[(cur_x, cur_y)] = set()
                paths[(cur_x, cur_y)].add(dir_num)
            
            cur_dir_num = (dir_num + 1) % 4
            temp1, temp2 = guard_dir[cur_dir_num]
            
            search(cur_x + dir_x, cur_y + dir_y, dir_x, dir_y, dir_num, paths)
            
            
    
    temp = get_dir_char(cur_dir)
    
    cur_dir_x, cur_dir_y = guard_dir[temp]
    
    search(guard_x, guard_y, cur_dir_x, cur_dir_y, temp, {})

print(len(positions))
print(output)
