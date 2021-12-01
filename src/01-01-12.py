import sys


def count_depth_measurement_increases(input_file_path="../inputs/01-01-12.txt", window_size=1):
    prev = sys.maxsize # float('inf')
    count = 0
    with open(input_file_path) as file:
        lines = [int(line.strip()) for line in file.readlines()]
        i = 0
        while(i <= len(lines)-window_size): # sliding window boundry
            window_start = i
            window_end = i + window_size - 1
            if window_start: # window_start !=0
                window_sum = window_sum - lines[window_start-1] + lines[window_end]
            else:
                window_sum = 0
                for w in range(window_size):
                    window_sum += lines[window_start + w]
            if window_sum > prev: count +=1
            prev = window_sum
            i +=1
    return count


if __name__ == '__main__':

    number_of_increases_w1 = count_depth_measurement_increases()
    print(number_of_increases_w1) # Answer:1462

    number_of_increases_w3 = count_depth_measurement_increases(window_size=3)
    print(number_of_increases_w3) # Answer:1497

