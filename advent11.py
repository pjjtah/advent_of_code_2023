with open("input11.txt") as f:
    lines = f.readlines()

add_space_x = []
add_space_y = []
galaxies = []
for x in range(0, len(lines)):
    if "#" not in lines[x]:
        add_space_x.append(x)
for y in range(0, len(lines[0])-1):
    empty = True
    for x in range(0, len(lines)):
        if lines[x][y] == "#":
            empty = False
            galaxies.append([y, x])
    if empty:
        add_space_y.append(y)

steps_p1 = 0
steps_p2 = 0
galaxies_done = []
for galaxy_from in galaxies:
    galaxies_done.append(galaxy_from)
    for galaxy_to in galaxies:
        if galaxy_to not in galaxies_done:
            min_y = min(galaxy_from[0], galaxy_to[0])
            max_y = max(galaxy_from[0], galaxy_to[0])
            min_x = min(galaxy_from[1], galaxy_to[1])
            max_x = max(galaxy_from[1], galaxy_to[1])
            y = max_y - min_y
            x = max_x - min_x
            steps_p1 += (x + y)
            steps_p2 += (x + y)
            for space in add_space_y:
                if min_y < space < max_y:
                    steps_p1 += 1
                    steps_p2 += 999999
            for space in add_space_x:
                if min_x < space < max_x:
                    steps_p1 += 1
                    steps_p2 += 999999


print("Part 1: " + str(steps_p1))
print("Part 2: " + str(steps_p2))
