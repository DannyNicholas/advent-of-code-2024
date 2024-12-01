import re

# read the provided text file and split columns into arrays of left/right numbers
def create_left_right_lists():
    with (open('left-right.txt', 'r') as file):
        left = []
        right = []
        for line in file:
            # Split each row on one or more whitespace characters
            columns = re.split(r'\s+', line.strip())
            left.append(int(columns[0]))
            right.append(int(columns[1]))
    return left, right

# sort both lists in order
# compare each left/right element to compute the differences
# sum all of these values
def sum_differences():
    left, right = create_left_right_lists()
    left.sort()
    right.sort()
    differences = [abs(a - b) for a, b in zip(left, right)]
    return sum(differences)

# multiply each left number by the frequency of that number in the right list
# sum all of these values
def sum_similarities():
    left, right = create_left_right_lists()
    similarities_sum = 0
    for num in left:
        count = right.count(num)
        similarities_sum += num * count
    return similarities_sum

# part 1
# should be 2264607
print("Part One:", sum_differences())

# part 2
# should be 19457120
print("Part Two:", sum_similarities())
