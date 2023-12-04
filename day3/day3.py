import re

IN_FILE = "in.txt"
REGEX_SYMBOLS = r"[*+#$@=%\/&-]"
REGEX_GEARS = r"[*]"
REGEX_NUMBERS = r"[0-9]+"


def extract_symbol_positions(lines):
    positions = []
    for i in range(len(lines)):
        positions.append([])
        for index in re.finditer(REGEX_GEARS, lines[i]):
            # print(index)
            # print(f"Start: {index.start()} | End: {index.end()}")
            positions[i].append(index.start())
    return positions


def determine_valid_parts(sub_boxes):
    valid_part_numbers = []
    for key in sub_boxes.keys():
        for number_string in sub_boxes[key]:
            symbols = re.findall(REGEX_SYMBOLS, number_string)
            if symbols == []:
                print(f"Symbols not found for key: {key}")
            else:
                valid_part_numbers.append(key)
    return valid_part_numbers


def extract_number_positions(lines):
    positions = []
    lengths = []
    part_nums = []
    for i in range(len(lines)):
        positions.append([])
        lengths.append([])
        part_nums.append([])
        for index in re.finditer(REGEX_NUMBERS, lines[i]):
            positions[i].append(index.start())
            lengths[i].append(index.end() - index.start())
            part_nums[i].append(int(index.group()))
    return positions, lengths, part_nums


def extract_sub_boxes(lines, number_locations, number_lengths, numbers):
    sub_boxes = {}  # number: box
    for engine_row_idx in range(
        len(number_locations)
    ):  # For each engine row with a number
        for part_number_idx in range(
            len(number_locations[engine_row_idx])
        ):  # For each part number in that row
            part_num_start = number_locations[engine_row_idx][part_number_idx]
            part_num_fin = (
                part_num_start + number_lengths[engine_row_idx][part_number_idx]
            )

            start_row = max(0, engine_row_idx - 1)
            start_column = max(0, part_num_start - 1)

            end_row = min(engine_row_idx + 2, LINE_LENGTH)
            end_column = min(part_num_fin + 1, LINE_LENGTH)

            box_str = ""
            for i in range(start_row, end_row):
                for j in range(start_column, end_column):
                    box_str += lines[i][j]

            if numbers[engine_row_idx][part_number_idx] in sub_boxes.keys():
                sub_boxes[numbers[engine_row_idx][part_number_idx]].append(box_str)
            else:
                sub_boxes[numbers[engine_row_idx][part_number_idx]] = [box_str]

    return sub_boxes


print(f"\n========== Game 1 ==========")
with open(IN_FILE, "r") as file:
    lines = file.readlines()
    number_locations, number_lengths, numbers = extract_number_positions(lines)
    LINE_LENGTH = len(lines[0].strip())
    sub_boxes = extract_sub_boxes(lines, number_locations, number_lengths, numbers)

    valid_part_numbers = determine_valid_parts(sub_boxes)

    print(sum(valid_part_numbers))


print(f"\n========== Game 2 ==========")
with open(IN_FILE, "r") as file:
    lines = file.readlines()
    symbol_locations = extract_symbol_positions(lines)
    LINE_LENGTH = len(lines[0].strip())
    number_locations, number_lengths, numbers = extract_number_positions(lines)
    print(f"Symb locations: {symbol_locations}")
    print(f"Num locations: {number_locations}")
    print(f"Num lengths: {number_lengths}")
    print(f"Part nums: {numbers}")
    adjacent_sum = 0
    for engine_row_idx in range(
        len(symbol_locations)
    ):  # For each engine row with a symbol
        
        for symbol_idx in range(
            len(symbol_locations[engine_row_idx])
        ):  # For each symbol in that row
            part_count_adjacent_to_symbol = 0
            print(f"Symbol idx: {symbol_idx}")
            symbol_position = symbol_locations[engine_row_idx][0]
            print(f"Symbol pos: {symbol_position}")

            # Iterate through the previous row
            previous_row = max(0, engine_row_idx - 1)
            adjacents = []
            # print(f"Prev row idx: {previous_row}")
            if not previous_row == engine_row_idx: # If the previous row is possible and not the current row
                for part_number_idx in range(len(number_locations[previous_row])):
                    part_number_min_pos = number_locations[previous_row][part_number_idx]
                    part_number_max_pos = part_number_min_pos + number_lengths[previous_row][part_number_idx]
                    print(f"Part min: {part_number_min_pos} | Part max: {part_number_max_pos}")

                    if bool(set(range(symbol_position - 1, symbol_position +2)) & set(range(part_number_min_pos, part_number_max_pos))):
                        part_count_adjacent_to_symbol += 1
                        print(f"Adjacent prev: {numbers[previous_row][part_number_idx]}")
                        adjacents.append(numbers[previous_row][part_number_idx])
            print()
            # Iterate through the current row
            current_row = engine_row_idx
            for part_number_idx in range(len(number_locations[current_row])):
                part_number_min_pos = number_locations[current_row][part_number_idx]
                part_number_max_pos = part_number_min_pos + number_lengths[current_row][part_number_idx]
                if bool(set(range(symbol_position - 1, symbol_position +2)) & set(range(part_number_min_pos, part_number_max_pos))):
                    part_count_adjacent_to_symbol += 1
                    adjacents.append(numbers[current_row][part_number_idx])
                    print(f"Adjacent curr: {numbers[current_row][part_number_idx]}")


            # Iterate through the next row
            # if not previous_row == engine_row_idx:
            next_row = min(engine_row_idx + 1, len(lines))
            for part_number_idx in range(len(number_locations[next_row])):
                part_number_min_pos = number_locations[next_row][part_number_idx]
                part_number_max_pos = part_number_min_pos + number_lengths[next_row][part_number_idx]
                if bool(set(range(symbol_position - 1, symbol_position +2)) & set(range(part_number_min_pos, part_number_max_pos))):
                    part_count_adjacent_to_symbol += 1
                    adjacents.append(numbers[next_row][part_number_idx])
                    print(f"Adjacent next: {numbers[next_row][part_number_idx]}")
            
            if part_count_adjacent_to_symbol !=2:
                continue
            else:
                print(f"Adj: {adjacents}")
                adjacent_sum += adjacents[0] * adjacents[1]
    print(f"Sum: {adjacent_sum}")