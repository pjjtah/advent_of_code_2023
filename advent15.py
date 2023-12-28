with open("input15.txt") as f:
    line = f.readline().rstrip()

sequences = line.split(",")
sequence_values = []
for sequence in sequences:
	current_value = 0
	for c in sequence:
		current_value += ord(c)
		current_value = current_value * 17
		current_value = current_value % 256
	sequence_values.append(current_value)

print("Part 1: " + str(sum(sequence_values)))