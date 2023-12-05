with open("input04.txt") as f:
    lines = f.readlines()

total_points = 0
copies = [1] * len(lines)
card_number = 0
for card in lines:
    card = card.rstrip()
    winning_numbers = card[card.find(":")+1:card.find("|")].split(" ")
    winning_numbers = [x for x in winning_numbers if x.isdigit()]
    numbers = card[card.find("|")+1:].split(" ")
    numbers = [x for x in numbers if x.isdigit()]
    points = 0
    matching = 0
    for number in numbers:
        if number in winning_numbers:
            matching += 1
            points = points * 2
            if points == 0:
                points = 1
    for i in range(1, copies[card_number]+1):
        for j in range(1, matching+1):
            copies[card_number + j] += 1
    card_number += 1
    total_points += points


print("Part 1: " + str(total_points))
print("Part 2: " + str(sum(copies)))
