def is_safe(line):
    n = len(line)
    increasing = all(1 <= line[i] - line[i - 1] <= 3 for i in range(1, len(line)))
    decreasing = all(-3 <= line[i] - line[i - 1] <= -1 for i in range(1, len(line)))
    return increasing or decreasing

def can_be_safe_with_dampener(line):
    for i in range(len(line)):
        modified_line = line[:i] + line[i + 1:]  
        if is_safe(modified_line):  
            return True
    return False

output = 0

with open("input.txt", 'r') as file:
    for line in file:
        levels = list(map(int, line.strip().split()))

        if is_safe(levels) or can_be_safe_with_dampener(levels):
            output += 1

print(output)