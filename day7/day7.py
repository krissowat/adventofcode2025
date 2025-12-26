def part_1(file):
    matrix = []
    for line in file:
        line = line.strip()
        matrix.append([char for char in line])
    splits = 0
    for i, line in enumerate(matrix):
        if i > 0:
            for j in range(len(matrix[0])):
                # Check for S
                if matrix[i-1][j] in ['S', '|']:
                    if matrix[i][j] != '^':
                        matrix[i][j] = '|'
                    else:
                        splits += 1
                        if j > 0 and matrix[i][j-1] != '^':
                            matrix[i][j-1] = '|'
                        if j < len(matrix[0]) - 1 and matrix[i][j+1] != '^':
                            matrix[i][j+1] = '|'
    return splits

if __name__ == "__main__":
    INPUT = 'input.txt'
    EXAMPLE = 'example.txt'
    with open(INPUT) as file:
        print(part_1(file))