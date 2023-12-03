import re

IN_FILE = "in.txt"

print(f"\n========== Game 1 ==========")
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
		no_chars = re.sub('[A-Za-z]', '', line)
		num = get_nums(no_chars)
		nums.append(num)
print(f"Out sum: {sum(nums)}")

print(f"\n========== Game 2 ==========")
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
print(f"Out sum: {sum(nums)}")