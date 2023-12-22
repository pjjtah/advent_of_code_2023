with open("input10.txt") as f:
    lines = f.readlines()


def check_nearby(fromY, fromX):
    up = "."
    down = "."
    left = "."
    right = "."
    if fromY > 0:
        up = lines[fromY - 1][fromX]
    if fromY < len(lines)-1:
        down = lines[fromY + 1][fromX]
    if fromX > 0:
        left = lines[fromY][fromX - 1]
    if fromX < len(lines[0])-1:
        right = lines[fromY][fromX + 1]
    poss = [False, False, False, False, False]
    pipe = lines[fromY][fromX]
    if pipe == "|" or pipe == "L" or pipe == "J":
        if up == "|" or up == "7" or up == "F" or down == "S":
            poss[0] = True
            if up == "S":
                poss[4] = True
    if pipe == "-" or pipe == "F" or pipe == "L":
        if right == "-" or right == "J" or right == "7" or down == "S":
            poss[1] = True
            if right == "S":
                poss[4] = True
    if pipe == "|" or pipe == "F" or pipe == "7":
        if down == "|" or down == "J" or down == "L" or down == "S":
            poss[2] = True
            if down == "S":
                poss[4] = True
    if pipe == "-" or pipe == "7" or pipe == "J":
        if left == "-" or left == "L" or left == "F" or down == "S":
            poss[3] = True
            if left == "S":
                poss[4] = True

    if pipe == "S":
        poss = [True, True, True, True]
        if up == ".":
            poss[0] = False
        if right == ".":
            poss[1] = False
        if down == ".":
            poss[2] = False
        if left == ".":
            poss[3] = False
    return poss


y = 0
x = 0
for line in lines:
    if "S" in line:
        x = line.index("S")
        break
    y = y+1

looped = False
possible = check_nearby(y,x)
visited = [[y, x]]
loop = []
if possible[0]:
    visited.append([y-1, x])
elif possible[1]:
    visited.append([y, x+1])
elif possible[2]:
    visited.append([y+1, x])
elif possible[3]:
    visited.append([y, x-1])
while not looped:
    x = visited[-1][1]
    y = visited[-1][0]
    possible = check_nearby(y, x)
    end = True
    if possible[0]:
        if [y-1, x] not in visited:
            visited.append([y-1, x])
            end = False
    if possible[1]:
        if [y, x+1] not in visited:
            visited.append([y, x+1])
            end = False
    if possible[2]:
        if [y+1, x] not in visited:
            visited.append([y+1, x])
            end = False
    if possible[3]:
        if [y, x-1] not in visited:
            visited.append([y, x-1])
            end = False
    if end:
        loop = visited
        looped = True
        break
print("Part 1: " + str(len(loop)//2))