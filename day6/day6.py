import math

def part_1(file):
    matrix = None
    grand_total = 0
    for line in file:
        numbers = line.split(' ')
        numbers = [number for number in numbers if number.strip()]
        if matrix is None:
            matrix = [[int(number)] for number in numbers]
        elif numbers[0] in ['*', '+']:
            for i, number in enumerate(numbers):
                if number == '*':
                    grand_total += math.prod(matrix[i])
                else:
                    grand_total += sum(matrix[i])
        else:
            for i, number in enumerate(numbers):
                matrix[i].append(int(number))
    return grand_total

def part_2(file):
    numbers = []
    for line in file:
        if line[0] not in ['*', '+']:
            for i, char in enumerate(line):
                if len(numbers) < i + 1:
                    numbers.append([])
                numbers[i] += char
        else:
            print(numbers)
            operators = [char for char in line if char in ['*', '+']]
            number_index = 0
            grand_total = 0
            for operator in operators:
                current_total = 1 if operator == '*' else 0
                while number_index < len(numbers):
                    number = ''.join(numbers[number_index])
                    number_index += 1
                    if number.strip() == '':
                        break
                    else:
                        if operator == '*':
                            current_total *= int(number)
                        else:
                            current_total += int(number)
                grand_total += current_total

    return grand_total


if __name__ == "__main__":
    INPUT = 'input.txt'
    EXAMPLE = 'example.txt'
    with open(INPUT) as file:
        print(part_2(file))