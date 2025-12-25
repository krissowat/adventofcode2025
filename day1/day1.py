def part_1(text):
    curr = 50
    zero_counter = 0
    for line in text:
        if len(line) > 1:
            if line[0] == 'L':
                curr -= int(line[1:])
            else:
                curr += int(line[1:])
            curr = curr % 100
            if curr == 0:
                zero_counter += 1
    return zero_counter

def part_2(text):
    curr = 50
    zero_counter = 0
    for line in text:
        if len(line) > 1:
            movement = int(line[1:])
            if line[0] == 'L':
                if movement > curr and curr != 0:
                    zero_counter += 1
                zero_counter += abs((curr - movement)) // 100
                curr -= movement
                if curr == 0:
                    zero_counter += 1
            else:
                zero_counter += (movement + curr) // 100
                curr += movement
            curr = curr % 100
    return zero_counter


if __name__ == "__main__":
    INPUT = 'input.txt'
    EXAMPLE = 'example.txt'
    with open(INPUT) as file:
        print(part_2(file))