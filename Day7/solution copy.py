import sys
sys.setrecursionlimit(10000)

output = [0]

with open("input.txt", "r") as input:
    
    for line in input:
        eq = line.strip()
        
        solution = ''
        idx = 0
        
        for i in range(len(eq)):
            if eq[i] == ':':
                idx = i + 2
                break
            else:
                solution += eq[i]
        
        solution = int(solution)
        
        possible = eq[idx:]
        possible = possible.split(' ')
        
        for i in range(len(possible)):
            possible[i] = int(possible[i])

        def find_sol(input, cur, sol, idx, n):
            if cur == sol and idx == n:
                return True
            if idx >= n or cur > sol:
                return False
            
            temp1 = find_sol(input, cur + input[idx], sol, idx + 1, n)
            temp2 = find_sol(input, cur * input[idx], sol, idx + 1, n)
            temp3 = False
            if cur == 0:
                temp3 = find_sol(input, input[idx], sol, idx + 1, n)
            else:
                temp3 = find_sol(input, int(str(cur) + str(input[idx])), sol, idx + 1, n)
            return temp1 or temp2 or temp3
        
        if find_sol(possible, 0, solution, 0, len(possible)):
            output[0] += solution

print(output)