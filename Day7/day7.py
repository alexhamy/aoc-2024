
import re

with open("input.txt", "r") as file:
    lines = file.readlines()


def solving(value, nums, current, n):
    if current == value and n==len(nums)-1:
        return True
    elif current != value and n == len(nums)-1:
        return False
    
    conc = str(current) + str(nums[n+1])
    return solving(value, nums, current + nums[n+1], n+1) or solving(value, nums, current * nums[n+1], n+1) or solving(value, nums, int(conc), n+1)

solution = 0
for i in lines:
    line = i.strip()
    line = line.split(": ")
    line[1] = line[1].split(" ")
    line[0] = int(line[0])
    new_line = []
    for j in line[1]:
        new_line.append(int(j))
    line[1] = new_line
    
    

    value = line[0]
    nums = line[1]
    

    if solving(value, nums, nums[0], 0):
        solution += value

    


print(solution)





