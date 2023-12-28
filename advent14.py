with open("input14.txt") as f:
    lines = f.readlines()

northest = [0] * (len(lines[0])-1)
y = 0
counter = 0
for line in lines:
	line = line.rstrip()
	for x in range(len(line)):
		if line[x] == "#":
			northest[x] = y + 1
		elif line[x] == "O":
			if northest[x] <= y:
				northest[x] += 1
				counter += len(lines) + 1  - northest[x]
			else:
				counter += len(lines) - y
	y += 1
print("Part 1: " + str(counter))