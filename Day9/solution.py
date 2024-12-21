import sys
sys.setrecursionlimit(10000)

output = [0]

input_str = '[]'

with open("input.txt", "r") as input:
    
    for line in input:
        eq = line.strip()
        input_str = eq
    
    print(input_str)
    
    
    
print(output)