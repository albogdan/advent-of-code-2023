import math
import re

IN_FILE = "in.txt"

print(f"\n========== Game 1 ==========")
total_pts = 0
with open(IN_FILE, "r") as file:
    lines = file.readlines()
    for line in lines:
        split_colon = line.strip().split(":")
        card_num = int(re.findall(r"[0-9]+", split_colon[0])[0])

        winning_nums, have_nums = split_colon[1].split("|")

        winning_nums = [int(x) for x in re.findall(r"[0-9]+", winning_nums)]
        have_nums = [int(x) for x in re.findall(r"[0-9]+", have_nums)]
        intersection = list(set(winning_nums) & set(have_nums))

        total_pts += math.floor(pow(2, len(intersection) - 1))

print(f"[PT1] Total pts: {total_pts}")

print(f"\n========== Game 2 ==========")
card_wins = {}

with open(IN_FILE, "r") as file:
    lines = file.readlines()
    for line in lines:
        split_colon = line.strip().split(":")
        card_num = int(re.findall(r"[0-9]+", split_colon[0])[0])
        if card_num in card_wins.keys():
            card_wins[card_num] += 1
        else:
            card_wins[card_num] = 1

        winning_nums, have_nums = split_colon[1].split("|")

        winning_nums = [int(x) for x in re.findall(r"[0-9]+", winning_nums)]
        have_nums = [int(x) for x in re.findall(r"[0-9]+", have_nums)]
        intersection = list(set(winning_nums) & set(have_nums))

        num_wins = len(intersection)
        for i in range(num_wins):
            card_to_add_to = i + card_num + 1

            if card_to_add_to in card_wins.keys():
                card_wins[card_to_add_to] += card_wins[card_num]
            else:
                card_wins[card_to_add_to] = card_wins[card_num]

print(f"[PT2] Sum of scratchcards: {sum(card_wins.values())}")
