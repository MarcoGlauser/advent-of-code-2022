
if __name__ == '__main__':
    filename = 'input.txt'
    max_calories = 0
    calories = 0
    with open(filename, 'r') as fp:

        for line in fp:
            if line == '\n':
                max_calories = max(calories, max_calories)
                calories = 0
            else:
                calories += int(line)
        if calories > 0:
            max_calories = max(calories, max_calories)
    print(max_calories)