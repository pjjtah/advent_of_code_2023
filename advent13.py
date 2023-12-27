with open("input13.txt") as f:
    lines = f.readlines()

patterns = [[]]

i = 0
for line in lines:
    if len(line.rstrip()) == 0:
        i += 1
        patterns.append([])
    else:
        patterns[i].append(line.rstrip())

vertical_mirrors = []
horizontal_mirrors = []
for pattern in patterns:
    for p in range(1, len(pattern[0])):
        vertical_mirrored = True
        for j in range(len(pattern)):
            left_pattern = pattern[j][:p]
            left_pattern = left_pattern[::-1]
            right_pattern = pattern[j][p:]
            length = min(len(left_pattern), len(right_pattern))
            if left_pattern[:length] != right_pattern[:length]:
                vertical_mirrored = False
                break
        if vertical_mirrored:
            vertical_mirrors.append(p)
            break
    for p in range(1, len(pattern)):
        up_pattern = pattern[:p]
        up_pattern = up_pattern[::-1]
        down_pattern = pattern[p:]
        length = min(len(up_pattern), len(down_pattern))
        if up_pattern[:length] == down_pattern[:length]:
            horizontal_mirrors.append(p * 100)
            break

print("Part 1: " + str(sum(vertical_mirrors) + sum(horizontal_mirrors)))

vertical_mirrors = []
horizontal_mirrors = []
for pattern in patterns:
    for p in range(1, len(pattern[0])):
        counter = 0
        for j in range(len(pattern)):
            left_pattern = pattern[j][:p]
            left_pattern = left_pattern[::-1]
            right_pattern = pattern[j][p:]
            length = min(len(left_pattern), len(right_pattern))
            for le in range(0, length):
                if left_pattern[le] != right_pattern[le]:
                    counter += 1
                if counter > 1:
                    break
            if counter > 1:
                break
        if counter == 1:
            vertical_mirrors.append(p)
            break
    for p in range(1, len(pattern)):
        up_pattern = pattern[:p]
        up_pattern = up_pattern[::-1]
        down_pattern = pattern[p:]
        length = min(len(up_pattern), len(down_pattern))
        counter = 0
        for le in range(0, length):
            for r in range(len(pattern[p])):
                if up_pattern[le][r] != down_pattern[le][r]:
                    counter += 1
                if counter > 1:
                    break
            if counter > 1:
                break
        if counter == 1:
            horizontal_mirrors.append(p * 100)
            break

print("Part 2: " + str(sum(vertical_mirrors) + sum(horizontal_mirrors)))
