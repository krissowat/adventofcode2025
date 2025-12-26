def part_1(file):
    max_joltage = 0
    for line in file:
        # Approach 1: Brute Force O(N^2)
        # bank_max = 0
        # for i in range(len(line)):
        #     for j in range(i+1, len(line)):
        #         bank_max = max(bank_max, int(line[i]+line[j]))
        # max_joltage += bank_max

        # Approach 2: O(N)
        # We can optimize the solution by doing two passes
        line = line.strip()
        tens_digit = max(line[:len(line)-1])
        tens_digit_index = line.index(tens_digit)
        ones_digit = max(line[tens_digit_index+1:len(line)])
        bank_max = int(tens_digit + ones_digit)
        max_joltage += bank_max

    return max_joltage

def part_2(file):
    max_joltage = 0
    for line in file:
        line = line.strip()
        number = ''
        i = 0
        max_digit_index = -1
        while i in range(12):
            search_line = line[max_digit_index+1:len(line)-11+i]
            max_digit = max(search_line)
            max_digit_index += 1 + search_line.index(max_digit)
            number += max_digit
            i += 1
        max_joltage += int(number)
        print(number)
    return max_joltage

if __name__ == "__main__":
    INPUT = 'input.txt'
    EXAMPLE = 'example.txt'
    with open(INPUT) as file:
        print(part_2(file))