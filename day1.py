import re

IN_FILE = "day1_in.txt"
""" Solution to Part 1
def remove_chars(line):
	temp = re.sub('[A-Za-z]', '', line)
	#print(temp)
	return temp

def get_nums(num_str):
	if len(num_str) > 1:
		return int(f"{num_str[0]}{num_str[-1]}")
	else:
		return int(f"{num_str}{num_str}")

nums = []

with open(IN_FILE, "r") as file:
	lines = file.readlines()
	for line in lines:
		line = line.strip('\n')

		no_chars = remove_chars(line)
		num = get_nums(no_chars)
		print(num)
		nums.append(num)

# Part 2 solution
number_text_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def remove_chars(line):
    for key in number_text_map.keys():
        if key in line:
            line = line.replace(key, f"{key[0]}{number_text_map[key]}{key[-1]}")

    temp = re.sub("[A-Za-z]", "", line)
    return temp


def get_nums(num_str):
    if len(num_str) > 1:
        return int(f"{num_str[0]}{num_str[-1]}")
    else:
        return int(f"{num_str}{num_str}")


nums = []

with open(IN_FILE, "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip("\n")

        no_chars = remove_chars(line)
        num = get_nums(no_chars)
        print(num)
        nums.append(num)

print(sum(nums))
"""
number_text_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
nums = []

with open(IN_FILE, "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip("\n")  # Remove newline char
        # Find text nums from dict and replace them with their first and last letter
        for key in number_text_map.keys():
            if key in line:
                line = line.replace(key, f"{key[0]}{number_text_map[key]}{key[-1]}")
        # Remove all chars a-z
        no_chars = re.sub("[A-Za-z]", "", line)
        if len(no_chars) > 1:  # Multi digit case
            num = int(f"{no_chars[0]}{no_chars[-1]}")
        else:  # Single digit case
            num = int(f"{no_chars}{no_chars}")
        nums.append(num)
print(sum(nums))
