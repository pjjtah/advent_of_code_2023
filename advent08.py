with open("input08.txt") as f:
    lines = f.readlines()

directions = lines[0].rstrip()
del lines[0]
del lines[0]
index = 0
i = 0
nodes = []
for line in lines:
    node = line[0:3]
    left = line[7:10]
    right = line[12:15]
    nodes.append([node, left, right])
    if node == "AAA":
        index = i
    i += 1
found = False
steps = 0
while not found:
    for direction in directions:
        steps += 1
        if direction == "L":
            next_node = nodes[index][1]
        elif direction == "R":
            next_node = nodes[index][2]
        else:
            next_node = ""
        if next_node == "ZZZ":
            found = True
            break
        for n in nodes:
            if n[0] == next_node:
                index = nodes.index(n)

print("Part 1:" + str(steps))
