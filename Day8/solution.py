import sys
sys.setrecursionlimit(10000)

output = [0]

graph = []

points_map = {}

stuff = set()

with open("input.txt", "r") as input:
    
    for line in input:
        eq = line.strip()
        graph.append(eq)
    
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            char = graph[i][j]
            if char != ".":
                if char not in points_map :
                    points_map[char] = [(j, i)]
                else:
                    points_map[char].append((j, i))
    
    max_x = len(graph[0])
    max_y = len(graph)
    
    
    def check(x, y):
        if x < 0 or x >= max_x or y < 0 or y >= max_y:
            return False
        else:
            return True
    
    for key in points_map:
        cords = points_map[key]
        for y in range(len(cords)):
            for x in range(y + 1, len(cords)):
                x_dif = cords[y][0] - cords[x][0]
                y_dif = cords[y][1] - cords[x][1]
                
                new_ant1 = (x_dif + cords[y][0], y_dif + cords[y][1])

                new_ant2 = (new_ant1[0] - (3*x_dif), new_ant1[1] - (3*y_dif))
                if check(new_ant1[0], new_ant1[1]):
                    stuff.add(new_ant1)
                if check(new_ant2[0], new_ant2[1]):
                    stuff.add(new_ant2)
                    
                
                

    print(points_map)
print(len(stuff))