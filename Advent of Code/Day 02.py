with open('Day 02.txt','r') as f:
    horizontal=0
    depth=0
    instructions=f.read().splitlines()
    for instruction in instructions:
        direction,quantity=instruction.split()
        quantity=int(quantity)
        if direction == "forward":
            horizontal+=quantity
        elif direction == "down":
            depth+=quantity
        else:
            depth-=quantity
print(horizontal*depth)

# Second Part

horizontal = 0
depth = 0
aim = 0

for instruction in instructions:
    direction,quantity=instruction.split()
    quantity=int(quantity)
    if direction == "forward":
        horizontal+=quantity
        if aim:
            depth = depth + (quantity*aim)
    elif direction == "down":
        aim += quantity
    else:
        aim -= quantity
print(horizontal*depth)