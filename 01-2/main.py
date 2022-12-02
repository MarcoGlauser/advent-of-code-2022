
if __name__ == '__main__':
    filename = 'input.txt'
    calories = 0
    elves = []
    with open(filename, 'r') as fp:
        for line in fp:
            if line == '\n':
                elves.append(calories)
                calories = 0
            else:
                calories += int(line)
        if calories > 0:
            elves.append(calories)
    elves.sort(reverse=True)
    print(sum(elves[0:3]))