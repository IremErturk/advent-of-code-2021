import sys

def count_depth_measurement_increases(input_file_path="../inputs/01-01-12.txt"):
    prev = sys.maxsize # float('inf')
    count = 0
    with open(input_file_path) as file:
        while (line := file.readline().strip()):
            if line:
                if int(line) > prev: count+=1
            prev = int(line)
    return count


if __name__ == '__main__':

    number_of_increases = count_depth_measurement_increases()
    print(number_of_increases) # Answer:1462


