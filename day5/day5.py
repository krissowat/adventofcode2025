def part_1(file):
    range = True
    fresh_ranges = []
    fresh_count = 0
    for line in file:
        if range:
            if (dash_index := line.find('-')) > 0:
                fresh_ranges.append((int(line[:dash_index]), int(line[(dash_index+1):])))
            else:
                range = False
        else:
            number = int(line)
            for fresh_range in fresh_ranges:
                if number >= fresh_range[0] and number <= fresh_range[1]:
                    fresh_count += 1
                    break
    return fresh_count

def part_2(file):
    fresh_ranges = []
    for line in file:
        if (dash_index := line.find('-')) > 0:
            fresh_ranges.append((int(line[:dash_index]), int(line[(dash_index+1):])))
        else:
            # We need to squash the ranges
            new_ranges = []
            i = 0
            while i < len(fresh_ranges):
                fresh_range = fresh_ranges[i]
                add_new_range = True
                for new_range in new_ranges:
                    add_new_range = True
                    # If range dominates other range, replace
                    if fresh_range[0] < new_range[0] and fresh_range[1] > new_range[1]:
                        new_ranges.remove(new_range)
                        fresh_ranges.append(fresh_range)
                        add_new_range = False
                        break
                    # only extends left side range
                    if fresh_range[0] < new_range[0] and fresh_range[1] >= new_range[0]:
                        new_ranges.remove(new_range)
                        fresh_ranges.append((fresh_range[0], new_range[1]))
                        add_new_range = False
                        break
                    # only extends right side range
                    if fresh_range[1] > new_range[1] and fresh_range[0] <= new_range[1]:
                        new_ranges.remove(new_range)
                        fresh_ranges.append((new_range[0], fresh_range[1]))
                        add_new_range = False
                        break
                    # is dominated by range
                    if fresh_range[0] >= new_range[0] and fresh_range[1] <= new_range[1]:
                        add_new_range = False
                        break
                if add_new_range:
                    new_ranges.append(fresh_range)
                i += 1

            fresh_ids = [new_range[1] - new_range[0] + 1 for new_range in new_ranges]
            return sum(fresh_ids)
    

if __name__ == "__main__":
    INPUT = 'input.txt'
    EXAMPLE = 'example.txt'
    with open(INPUT) as file:
        print(part_2(file))