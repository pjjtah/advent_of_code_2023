with open("input01.txt") as f:
    lines = f.readlines()

# part 1
values = []
for line in lines:
    first_digit = ""
    last_digit = ""
    for character in line:
        if character.isnumeric():
            if first_digit == "":
                first_digit = character
            last_digit = character
    values.append(str(first_digit) + str(last_digit))

total_value = 0
for v in values:
    if v.isnumeric():
        total_value += int(v)

print("Part 1: " + str(total_value))

# part 2
values = []
spelled_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for line in lines:
    first_digit = ""
    first_digit_index = -1
    last_digit = ""
    last_digit_index = -1
    counter = 0
    for character in line:
        if character.isnumeric():
            if first_digit_index == -1:
                first_digit_index = counter
                first_digit = character
            last_digit = character
            last_digit_index = counter
        counter += 1

    # check if first number is spelled
    counter = 0
    if first_digit_index == -1:
        first_digit_index = len(line)
    for s in spelled_numbers:
        counter += 1
        i = line.find(s)
        if i != -1 and i < first_digit_index:
            first_digit_index = i
            first_digit = counter

    # check if last number is spelled
    counter = 0
    for s in spelled_numbers:
        counter += 1
        i = line.rfind(s)
        if i != -1 and i > last_digit_index:
            last_digit_index = i
            last_digit = counter

    values.append(str(first_digit) + str(last_digit))

total_value = 0
for v in values:
    total_value += int(v)

print("Part 2: " + str(total_value))