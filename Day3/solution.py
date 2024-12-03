output = 0

arr = []

nums = ('1','2','3','4','5','6','7','8','9','0', ',')

with open("input.txt", "r") as input:
    content = input.read()
    
    do = True
    
    n = len(content)
    i = 0
    while i < n:
        if content[i:i+4] == 'do()':
            do = True
            print("do")
            i += 1
        if content[i:i+7] == "don't()":
            do = False
            print("dont")
            i += 1
            
        if do:
            if content[i:i+3] == 'mul':
                i += 3
                num1 = ''
                num2 = ''
                
                if content[i] != '(':
                    continue
                i += 1
                
                broken = True
                
                for j in range(3):
                    if(content[i + j] not in nums):
                        i += j
                        broken = False
                        break
                    if content[i + j] == ',':
                        i += j
                        broken = False
                        break
                    num1 += str(content[j + i])
                
                if broken:
                    i += 3
                
                if(content[i] != ','):
                    continue
                
                i += 1
                
                broken = True
                
                for j in range(3):
                    if(content[i + j] not in nums):
                        i += j
                        broken = False
                        break
                    if content[i + j] == ',':
                        i += j
                        broken = False
                        break
                    num2 += str(content[j + i])
                
                if broken:
                    i += 3
                    
                if content[i] != ')':
                    continue
                
                output += int(num1) * int(num2)
        
        i += 1
    
print(output)