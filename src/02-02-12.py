import sys


def find_position_v1(input_file_path="../inputs/02-02-12.txt"):
    horizontal_position, depth = 0, 0
    with open(input_file_path) as file:
        while (line := file.readline().strip()):
            direction, unit = line.split(" ")
            if direction == "forward":
                horizontal_position += int(unit)
            else:
                if direction == "up":
                    depth -= int(unit)
                else:
                    depth += int(unit)
    return horizontal_position, depth


def find_position_v2(input_file_path="../inputs/02-02-12.txt"):
    
    horizontal_position, depth, aim = 0, 0, 0

    with open(input_file_path) as file:
        while (line := file.readline().strip()):
            direction, unit = line.split(" ")
            if direction == "forward":
                horizontal_position += int(unit)
                depth += (aim*int(unit))
            else:
                if direction == "up":
                    aim -= int(unit)
                else:
                    aim += int(unit)
    return horizontal_position, depth


if __name__ == '__main__':

    horizontal_position, depth = find_position_v1()
    print(horizontal_position * depth) # 1561344

    horizontal_position, depth = find_position_v2()
    print(horizontal_position * depth) # 1848454425

