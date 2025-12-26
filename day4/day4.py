def part_1(file):
    lines = []
    for line in file:
        lines.append(line.strip())

    rolls = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '@':
                surrounding_rolls = 0
                if i > 0 and lines[i-1][j] == '@':
                    # top
                    surrounding_rolls += 1
                if i > 0 and j > 0 and lines[i-1][j-1] == '@':
                    # top left
                    surrounding_rolls += 1
                if i > 0 and j < len(lines[0]) - 1 and lines[i-1][j+1] == '@':
                    # top right
                    surrounding_rolls += 1
                if j > 0 and lines[i][j-1] == '@':
                    # left
                    surrounding_rolls += 1
                if j < len(lines[0]) - 1 and lines[i][j+1] == '@':
                    # right
                    surrounding_rolls += 1
                if i < len(lines) - 1 and lines[i+1][j] == '@':
                    # bottom
                    surrounding_rolls += 1
                if i < len(lines) - 1 and j > 0 and lines[i+1][j-1] == '@':
                    # bottom left
                    surrounding_rolls += 1
                if i < len(lines) - 1 and j < len(lines[0]) - 1 and lines[i+1][j+1] == '@':
                    # top right
                    surrounding_rolls += 1
                if surrounding_rolls < 4:
                    rolls += 1
    return rolls



if __name__ == "__main__":
    INPUT = 'input.txt'
    EXAMPLE = 'example.txt'
    with open(INPUT) as file:
        print(part_1(file))