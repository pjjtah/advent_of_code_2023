with open("input02.txt") as f:
    lines = f.readlines()

# part 1
id_sum = 0
power_sum = 0
colors = ["red", "green", "blue"]
maximums = [12, 13, 14]
for line in lines:
    possible = True
    start = line.find(":")
    game_id = int(line[5: start])
    min_cubes = [0, 0, 0]
    cube_sets = line[start+1:].split(";")
    cube_sets.append(line[line.rfind(";")+1:])
    for cube_set in cube_sets:
        cubes = cube_set.split(",")
        for cube in cubes:
            i = 0
            for color in colors:
                if color in cube:
                    amount = int(cube[cube.find(" "): cube.rfind(" ")])
                    if amount > min_cubes[i]:
                        min_cubes[i] = amount
                    if amount > maximums[i]:
                        possible = False
                i += 1
    if possible:
        id_sum += game_id
    power = 1
    for m in min_cubes:
        power = power * m
    power_sum += power

print("Part 1: " + str(id_sum))
print("Part 2: " + str(power_sum))

# part 1

