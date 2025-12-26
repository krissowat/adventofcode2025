import copy

def part_1(file):
    matrix = []
    for line in file:
        line = line.strip()
        matrix.append([char for char in line])
    
    def get_timelines(i, matrix):
        timelines = 0
        while i < len(matrix):
            j = 0
            while j < len(matrix[0]):
                # Check for S
                if matrix[i-1][j] in ['S', '|']:
                    if matrix[i][j] != '^':
                        matrix[i][j] = '|'
                    else:
                        if j > 0 and matrix[i][j-1] != '^':
                            # Left timeline
                            left_matrix = copy.deepcopy(matrix)
                            left_matrix[i][j-1] = '|'
                            timelines += get_timelines(i+1, left_matrix)
                        if j < len(matrix[0]) - 1 and matrix[i][j+1] != '^':
                            # Right timeline
                            matrix[i][j+1] = '|'
                            timelines += get_timelines(i+1, matrix)
                        return timelines
                j += 1
            i += 1
        return 1
    
    return get_timelines(1, matrix)

if __name__ == "__main__":
    INPUT = 'input.txt'
    EXAMPLE = 'example.txt'
    with open(INPUT) as file:
        print(part_1(file))