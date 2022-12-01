def main():
    sorted_elves = sorted(get_elves())
    print(f'Answer 1: {sorted_elves[-1]}')
    print(f'Answer 2: {sum(sorted_elves[-3:])}')

def get_elves():
    with open('input.txt') as input:
        lines = input.readlines()
    result = []
    elve = []
    for line in lines:
        if not line.strip():
            result.append(elve)
            elve = []
        else:
            elve.append(int(line))
    if elve:
        result.append(elve)
    return [sum(value) for value in result]


if __name__ == '__main__':
    main()
