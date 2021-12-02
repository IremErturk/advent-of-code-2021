import sys


def find_position(input_file_path="../inputs/02-02-12.txt"):
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



if __name__ == '__main__':

    horizontal_position, depth = find_position()
    print(horizontal_position * depth) # 1561344

