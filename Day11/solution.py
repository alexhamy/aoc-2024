import sys
import functools
sys.setrecursionlimit(10000)

result = [0]

inp = ''

cache = {}

with open("input.txt", "r") as input:
    
    for line in input:
        eq = line.strip()
        inp = eq 
    
    arr = eq.split(' ')
    
    
    @functools.cache
    def blink(num):
        
        output = []
        
        new = str(num)
        n = len(new)
        
        if num == 0:
            output.append(1)
            return output
        
        if n % 2 == 0:
            
            if num in cache:
                return cache[num]
            
            n = n//2
            
            output.append(int(new[:n]))
            output.append(int(new[n:]))
            
            cache[num] = output
            
            return output
                
        else:
            output.append(num*2024)
            return output
        
    
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    
    n = 0
    
    for i in range(75):
        j = 0
        n = len(arr)
        while(j < n):
            num = arr[j]
            out = blink(num)
            if len(out) == 1:
                arr[j] = out[0]
            else:
                arr[j] = out[0]
                arr.insert(j + 1, out[1])
                n += 1
                j += 1
                
            j += 1
        print(i)
    print(n)