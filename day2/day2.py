def part_1(file):
    first_num = ''
    second_num = ''
    is_second = False

    def sum_invalid_IDs(first_num: str, second_num: str):
        invalid_id_sum = 0
        for number in range(int(first_num), int(second_num) + 1):
            number_str = str(number)
            if number_str[0:len(number_str)//2] == number_str[len(number_str)//2:]:
                invalid_id_sum += number
        return invalid_id_sum

    total_sum = 0
    for line in file:
        for char in line:
            # Check for end of range
            if char == ',':
                total_sum += sum_invalid_IDs(first_num, second_num)
                first_num = ''
                second_num = ''
                is_second = False
            elif char == "-":
                is_second = True
            else:
                if is_second:
                    second_num += char
                else:
                    first_num += char
    total_sum += sum_invalid_IDs(first_num, second_num)
    return total_sum
        

def part_2(file):
    first_num = ''
    second_num = ''
    is_second = False

    def sum_invalid_IDs(first_num: str, second_num: str):
        invalid_id_sum = 0
        for number in range(int(first_num), int(second_num) + 1):
            is_invalid = False
            number_str = str(number)
            for i in range(1, len(number_str)):
                if is_invalid:
                    continue
                # Iterates 1 ... len - 1 for starting position possibilities
                if len(number_str) % i != 0:
                    # Skip if the number cannot be evenly divided into i portions
                    continue
                start_number_str = number_str[:i]
                start_number_len = len(start_number_str)
                for j in range(len(number_str)//i):
                    # Iterates over # divided portions (123123 -> 123 | 123)
                    if number_str[i*j:i*j+start_number_len] != start_number_str:
                        break
                    if j == len(number_str)//i - 1:
                        is_invalid = True
                        invalid_id_sum += number

                
        return invalid_id_sum

    total_sum = 0
    for line in file:
        for char in line:
            # Check for end of range
            if char == ',':
                total_sum += sum_invalid_IDs(first_num, second_num)
                first_num = ''
                second_num = ''
                is_second = False
            elif char == "-":
                is_second = True
            else:
                if is_second:
                    second_num += char
                else:
                    first_num += char
    total_sum += sum_invalid_IDs(first_num, second_num)
    return total_sum
        

if __name__ == "__main__":
    INPUT = 'input.txt'
    EXAMPLE = 'example.txt'
    with open(INPUT) as file:
        print(part_2(file))