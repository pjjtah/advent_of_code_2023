with open("input16.txt") as f:
    lines = f.readlines()

tiles = []
i = 0
for line in lines:
    tiles.append([])
    for li in line.rstrip():
        tiles[i].append(li)
    i += 1
energized = []
rays = [[0, 0]]


def beam(coordinates):
    if coordinates not in energized:
        energized.append(coordinates)
    current = tiles[coordinates[0]][coordinates[1]]
    if coordinates[0] > 0:
        if "^" not in tiles[coordinates[0] - 1][coordinates[1]]:
            if (((">" in current or "<" in current) and "|" in current)
                    or (">" in current and "/" in current)
                    or ("<" in current and "\\" in current)
                    or ("^" in current and ("." in current or "|" in current))):
                tiles[coordinates[0] - 1][coordinates[1]] += "^"
                rays.append([coordinates[0] - 1, coordinates[1]])
    if coordinates[0] < len(lines) - 1:
        if "v" not in tiles[coordinates[0] + 1][coordinates[1]]:
            if (((">" in current or "<" in current) and "|" in current)
                    or (">" in current and "\\" in current)
                    or ("<" in current and "/" in current)
                    or ("v" in current and ("." in current or "|" in current))):
                tiles[coordinates[0] + 1][coordinates[1]] += "v"
                rays.append([coordinates[0] + 1, coordinates[1]])
    if coordinates[1] > 0:
        if "<" not in tiles[coordinates[0]][coordinates[1] - 1]:
            if ((("^" in current or "v" in current) and "-" in current)
                    or ("^" in current and "\\" in current)
                    or ("v" in current and "/" in current)
                    or ("<" in current and ("." in current or "-" in current))):
                tiles[coordinates[0]][coordinates[1] - 1] += "<"
                rays.append([coordinates[0], coordinates[1] - 1])
    if coordinates[1] < len(tiles[coordinates[0]]) - 1:
        if ">" not in tiles[coordinates[0]][coordinates[1] + 1]:
            if ((("^" in current or "v" in current) and "-" in current)
                    or ("^" in current and "/" in current)
                    or ("v" in current and "\\" in current)
                    or (">" in current and ("." in current or "-" in current))):
                tiles[coordinates[0]][coordinates[1] + 1] += ">"
                rays.append([coordinates[0], coordinates[1] + 1])


# 0 up, 1 right, 2 down, 3 left
tiles[0][0] += ">"
while len(rays) > 0:
    r = rays.pop()
    beam(r)
print("Part 1: " + str(len(energized)))
energized_possible = []
for y in range(len(tiles)-1):
    tiles = []
    i = 0
    for line in lines:
        tiles.append([])
        for li in line.rstrip():
            tiles[i].append(li)
        i += 1
    tiles[y][0] += ">"
    rays = [[y, 0]]
    energized = []
    while len(rays) > 0:
        r = rays.pop()
        beam(r)
    energized_possible.append(len(energized))
    tiles = []
    i = 0
    for line in lines:
        tiles.append([])
        for li in line.rstrip():
            tiles[i].append(li)
        i += 1
    tiles[y][len(tiles[y])-1] += "<"
    rays = [[y, len(tiles[y])-1]]
    energized = []
    while len(rays) > 0:
        r = rays.pop()
        beam(r)
    energized_possible.append(len(energized))
for x in range(len(tiles[0])-1):
    tiles = []
    i = 0
    for line in lines:
        tiles.append([])
        for li in line.rstrip():
            tiles[i].append(li)
        i += 1
    tiles[0][x] += "v"
    rays = [[0, x]]
    energized = []
    while len(rays) > 0:
        r = rays.pop()
        beam(r)
    energized_possible.append(len(energized))
    tiles = []
    i = 0
    for line in lines:
        tiles.append([])
        for li in line.rstrip():
            tiles[i].append(li)
        i += 1
    tiles[len(tiles[x])-1][0] += "^"
    rays = [[len(tiles[x])-1, x]]
    energized = []
    while len(rays) > 0:
        r = rays.pop()
        beam(r)
    energized_possible.append(len(energized))
print("Part 2: " + str(max(energized_possible)))