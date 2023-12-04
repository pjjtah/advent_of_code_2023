with open("input03.txt") as f:
    lines = f.readlines()


class Gear:
    def __init__(self, pos_x, pos_y, near):
        self.pos_x = pos_x,
        self.pos_y = pos_y,
        self.near = near


x = 0
y = 0
result = 0
positions = [[1, 1], [1, 0], [1, -1], [0, 1], [0, -1], [-1, 1], [-1, 0], [-1, -1]]
gears = []
for line in lines:
    line = line.rstrip()
    symbol_near = False
    number = ""
    x = 0
    nearby_gears = []
    for character in line:
        if character.isdigit():
            number += character
            for position in positions:
                check_x = x + position[0]
                check_y = y + position[1]
                if 0 < check_x < len(line) and 0 < check_y < len(lines):
                    if (not lines[check_y][check_x].isdigit()) and lines[check_y][check_x] != ".":
                        symbol_near = True
                        if lines[check_y][check_x] == "*":
                            gear_exists = False
                            for gear in nearby_gears:
                                if gear[0] == check_y and gear[1] == check_x:
                                    gear_exists = True
                                    break
                            if not gear_exists:
                                nearby_gears.append([check_y, check_x])
        else:
            if symbol_near:
                result += int(number)
                if len(nearby_gears) > 0:
                    for gear in nearby_gears:
                        gear_exists = False
                        for g in gears:
                            if gear[1] == g.pos_y[0] and gear[0] == g.pos_x[0]:
                                g.near.append(number)
                                gear_exists = True
                                break
                        if not gear_exists:
                            gears.append(Gear(gear[0], gear[1], [number]))
            symbol_near = False
            number = ""
            nearby_gears = []
        x += 1
    if symbol_near:
        result += int(number)
        if len(nearby_gears) > 0:
            for gear in nearby_gears:
                gear_exists = False
                for g in gears:
                    if gear[1] == g.pos_y[0] and gear[0] == g.pos_x[0]:
                        g.near.append(number)
                        gear_exists = True
                        break
                if not gear_exists:
                    gears.append(Gear(gear[0], gear[1], [number]))
    y += 1
print("Part 1:" + str(result))

ratio_sum = 0
for gear in gears:
    print(gear.near)
    if len(gear.near) == 2:
        ratio_sum += int(gear.near[0]) * int(gear.near[1])
print("Part 2:" + str(ratio_sum))