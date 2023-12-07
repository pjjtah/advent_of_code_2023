with open("input06.txt") as f:
    lines = f.readlines()

times = lines[0].rstrip()[lines[0].find(":"):].split(" ")
times = [x for x in times if x.isdigit()]
distances = lines[1].rstrip()[lines[1].find(":"):].split(" ")
distances = [x for x in distances if x.isdigit()]


def calculate_ways(time, record):
    distance = 0
    time_held = 0
    speed = 0
    while distance <= int(record):
        time_held += 1
        speed += 1
        distance = (int(time) - time_held) * speed
    start = time_held
    distance = 0
    time_held = int(time)
    speed = int(time)
    while distance <= int(record):
        time_held -= 1
        speed -= 1
        distance = (int(time) - time_held) * speed
    end = time_held + 1
    return end - start


ways = 1
i = 0
no_space_time = ""
no_space_distance = ""
for t, r in zip(times, distances):
    no_space_time += t
    no_space_distance += r
    ways = ways * calculate_ways(t, r)
    i += 1


print("Part 1: " + str(ways))

print("Part 2 : " + str(calculate_ways(int(no_space_time), int(no_space_distance))))
