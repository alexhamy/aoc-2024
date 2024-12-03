output = 0

arr1 = []
arr2 = []

with open("input.txt", "r") as input:
    for line in input:
        temp = line.strip()
        temp = temp.split(' ')
        arr1.append(int(temp[0]))
        arr2.append(int(temp[3]))

arr1.sort()
arr2.sort()
    
n = len(arr1)

counter = {}

for i in range(n):
    num = arr2[i]
    if num not in counter:
        counter[num] = 1
    else:
        counter[num] += 1

for i in range(n):
    num = arr1[i]
    if num in counter:
        output += num * counter[num]
