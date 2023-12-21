with open("input09.txt") as f:
    lines = f.readlines()

value_histories = []
for line in lines:
    value_histories.append([int(x) for x in line.rstrip().split(" ")])

predictions = []
for values in value_histories:
    differences = [values]
    sequence = 0
    i = 0
    all_zeroes = False
    while not all_zeroes:
        differences.append([])
        for i in range(1, len(differences[sequence])):
            difference = differences[sequence][i] - differences[sequence][i - 1]
            differences[sequence + 1].append(difference)
        sequence += 1
        if sum(differences[sequence]) == 0:
            all_zeroes = True
            for i in range(len(differences) - 1, 0, -1):
                prediction = differences[i][len(differences[i]) - 1] + differences[i - 1][len(differences[i - 1]) - 1]
                differences[i - 1].append(prediction)
                if i == 1:
                    predictions.append(prediction)

print("Part 1: " + str(sum(predictions)))
