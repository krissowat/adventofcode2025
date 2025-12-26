def part_1(file):
    lines = []
    for line in file:
        lines.append(line.strip())

    rolls = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            rolls += 1 if can_be_removed(lines, i, j) else 0
    return rolls

def can_be_removed(lines, i, j):
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
            return True
    return False

def part_2(file):
    lines = []
    for line in file:
        lines.append([c for c in line.strip()])

    def remove(i, j):
        if lines[i][j] == '@':
            surrounding_rolls = 0
            surrounding_roll_indices = []
            if i > 0 and lines[i-1][j] == '@':
                # top
                surrounding_rolls += 1
                surrounding_roll_indices.append((i-1, j))
            if i > 0 and j > 0 and lines[i-1][j-1] == '@':
                # top left
                surrounding_rolls += 1
                surrounding_roll_indices.append((i-1, j-1))
            if i > 0 and j < len(lines[0]) - 1 and lines[i-1][j+1] == '@':
                # top right
                surrounding_rolls += 1
                surrounding_roll_indices.append((i-1, j+1))
            if j > 0 and lines[i][j-1] == '@':
                # left
                surrounding_rolls += 1
                surrounding_roll_indices.append((i, j-1))
            if j < len(lines[0]) - 1 and lines[i][j+1] == '@':
                # right
                surrounding_rolls += 1
                surrounding_roll_indices.append((i, j+1))
            if i < len(lines) - 1 and lines[i+1][j] == '@':
                # bottom
                surrounding_rolls += 1
                surrounding_roll_indices.append((i+1, j))
            if i < len(lines) - 1 and j > 0 and lines[i+1][j-1] == '@':
                # bottom left
                surrounding_rolls += 1
                surrounding_roll_indices.append((i+1, j-1))
            if i < len(lines) - 1 and j < len(lines[0]) - 1 and lines[i+1][j+1] == '@':
                # top right
                surrounding_rolls += 1
                surrounding_roll_indices.append((i+1, j+1))
            if surrounding_rolls < 4:
                lines[i][j] = '.'
                return 1 + sum([remove(index[0], index[1]) for index in surrounding_roll_indices])
        return 0

    rolls = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            rolls += remove(i, j)
    return rolls

if __name__ == "__main__":
    INPUT = 'input.txt'
    EXAMPLE = 'example.txt'
    with open(INPUT) as file:
        print(part_2(file))