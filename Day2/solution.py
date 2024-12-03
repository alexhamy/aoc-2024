output = 0

with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip()
        line = line.split(' ')
        
        for i in range(len(line)):
            line[i] = int(line[i])
        
        increasing  = True
            
        avg_dif = 0
        
        for i in range(1, len(line)):
            dif = line[i] - line[i-1]
            if dif <= 0:
                avg_dif += 1
        
        if avg_dif > len(line) - 3:
            increasing = False
            
        
        complete = True
        
        dampaner = True
        
        i = 1
        
        n = len(line)
        
        if increasing:
            while i < n:
                dif = line[i] - line[i - 1]
                if dif >= 1 and dif <=3:
                    i += 1
                elif dampaner:
                    line[i] < line[i - 1]
                    i = 1
                    n -= 1
                    dampaner = False
                else:
                    complete = False
                    break
                
        else:
            while i < n:
                dif = line[i] - line[i - 1]
                if dif <= -1 and dif >= -3:
                    i += 1
                elif dampaner:
                    line.pop(i)
                    i = 1
                    n -= 1
                    dampaner = False
                else:
                    complete = False
                    break
        
        if complete:
            output += 1
            
        
        
print(output)