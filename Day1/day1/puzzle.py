def puzzle():
    sorted_calories = sorted([elve.sum() for elve in get_elves()])
    print(f'Answer 1: {sorted_calories[-1]}')
    print(f'Answer 2: {sum(sorted_calories[-3:])}')

def get_elves():
    with open('input.txt') as input:
        lines = input.readlines()
    result = []
    elve = Elve()
    for line in lines:
        if not line.strip():
            result.append(elve)
            elve = Elve()
        else:
            elve.append(int(line))
    if elve.sum():
        result.append(elve)
    return result

class Elve:
    def __init__(self):
        self.food = []
    
    def sum(self):
        return sum(self.food)
    
    def append(self, food):
        self.food.append(food)


if __name__ == '__main__':
    puzzle()
