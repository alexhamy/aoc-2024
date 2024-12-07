output = 0

rules = {}

arr = []

arr_rules = []

arr_order = []

wrong = []

def check_order(input_arr):
    for i in range(len(input_arr)):
        for j in range(len(input_arr)):
            if input_arr[i] in rules:
                if input_arr[j] in rules[input_arr[i]]:
                    if j < i:
                        temp = input_arr[i]
                        input_arr[i] = input_arr[j]
                        input_arr[j] = temp
                        check_order(input_arr)
    return input_arr
with open("input.txt", "r") as input:
    
    flip = True
    
    for line in input:
        temp = line.strip()
        
        if temp == '':
            flip = False
        elif flip:
            arr_rules.append(temp)
        else:
            arr_order.append(temp)
    
    for rule in arr_rules:
        sep = rule.split('|')
        
        if int(sep[0]) not in rules:
            rules[int(sep[0])] = {int(sep[1])}
        else:
            rules[int(sep[0])].add(int(sep[1]))
        
    for order in arr_order:
        sep_order = order.split(',')
        
        for i in range(len(sep_order)):
            sep_order[i] = int(sep_order[i])
        
        check = True
        
        for i in range(len(sep_order)):
            for j in range(len(sep_order)):
                if sep_order[i] in rules:
                    if sep_order[j] in rules[sep_order[i]]:
                        if j < i:
                            check = False
                            break
        if check:
            output += sep_order[len(sep_order)//2]
            
        else:
            wrong.append(sep_order)
    print(output)
    output = 0
    for i in range(len(wrong)):
        temp = check_order(wrong[i])
        output += temp[len(temp)//2]
        
        

print(output)
