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
    matrix = None
    grand_total = 0
    for line in file:
        numbers = line.split(' ')
        numbers = [number for number in numbers if number.strip()]
        if matrix is None:
            matrix = [[int(number)] for number in numbers]
        elif numbers[0] in ['*', '+']:
            for i, operation in enumerate(numbers):
                # Re-order the numbers correctly
                wrong_numbers = matrix[i]
                correct_numbers = []
                while sum(wrong_numbers) != 0:
                    correct_number = 0
                    for i in range(len(wrong_numbers)):
                        correct_number = correct_number * 10 + wrong_numbers[i]%10 if wrong_numbers[i] != 0 else correct_number
                        wrong_numbers[i] = wrong_numbers[i]//10
                    correct_numbers.append(correct_number)
                print(correct_numbers)
                if operation == '*':
                    grand_total += math.prod(correct_numbers)
                else:
                    grand_total += sum(correct_numbers)
        else:
            for i, number in enumerate(numbers):
                matrix[i].append(int(number))
    return grand_total


if __name__ == "__main__":
    INPUT = 'input.txt'
    EXAMPLE = 'example.txt'
    with open(EXAMPLE) as file:
        print(part_2(file))