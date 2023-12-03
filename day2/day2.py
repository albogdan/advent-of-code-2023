import re

IN_FILE = "in.txt"

colours = {"red": 0, "green": 1, "blue": 2}
def isolate_rgb(set):
    rgb_raw_list = set.split(",")
    out = {}
    for rgb_text in rgb_raw_list:
        count = int(re.findall(r"\d+", rgb_text)[0])
        colour = [x for x in colours.keys() if x in rgb_text][0]
        out[colour] = count
    return out

print(f"\n========== Game 1 ==========")
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14
valid_games = []
with open(IN_FILE, "r") as file:
    lines = file.readlines()
    for line in lines:
        game_success = True
        game,sets = line.strip('\n').split(":")
        game_id = game.split(" ")[1]

        for set in sets.split(";"):
            rgb_counts = isolate_rgb(set)

            if "red" in rgb_counts and rgb_counts["red"] > MAX_RED:
                 game_success = False
                 break

            if "green" in rgb_counts and rgb_counts["green"] > MAX_GREEN:
                 game_success = False
                 break

            if "blue" in rgb_counts and rgb_counts["blue"] > MAX_BLUE:
                 game_success = False
                 break
        if game_success:
            valid_games.append(int(game_id))

print(f"Out 1: {(valid_games)}")
print(f"Out sum 1: {sum(valid_games)}")

print(f"\n========== Game 2 ==========")
game_power = []
with open(IN_FILE, "r") as file:
    lines = file.readlines()
    for line in lines:
        game_success = True
        game, sets = line.strip("\n").split(":")
        game_id = game.split(" ")[1]

        current_red = 0
        current_green = 0
        current_blue = 0

        for set in sets.split(";"):
            rgb_counts = isolate_rgb(set)

            if "red" in rgb_counts and rgb_counts["red"] > current_red:
                current_red = rgb_counts["red"]

            if "green" in rgb_counts and rgb_counts["green"] > current_green:
                current_green = rgb_counts["green"]

            if "blue" in rgb_counts and rgb_counts["blue"] > current_blue:
                current_blue = rgb_counts["blue"]

        game_power.append(current_red * current_green * current_blue)

print(f"Out 2: {(game_power)}")
print(f"Out sum 2: {sum(game_power)}")
