with open("input05.txt") as f:
    lines = f.readlines()

seeds = lines[0].rstrip()[lines[0].find(":"):].split(" ")
seeds = [x for x in seeds if x.isdigit()]
lines.pop(0)
maps = []
counter = -1
for line in lines:
    if "map" in line:
        counter += 1
        maps.append([])
    elif line != "\n":
        maps[counter].append(line.rstrip().split(" "))

seed_locations = []
for seed in seeds:
    value = int(seed)
    for m in maps:
        for r in m:
            r = [int(x) for x in r]
            if r[1] <= value < r[1]+r[2]:
                value = (value - r[1]) + r[0]
                break
    seed_locations.append(value)


print("Part 1: " + str(min(seed_locations)))

