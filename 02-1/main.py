score = {
    'A': 1,
    'B': 2,
    'C': 3
}

win_condition ={
    'A': 'C',
    'B': 'A',
    'C': 'B'
}


if __name__ == '__main__':
    filename = 'input.txt'

    with open(filename, 'r') as fp:
        total_score = 0
        for line in fp:
            opponent, me = line.strip().split(' ')
            my_move = chr(ord(me) -23)
            total_score += score[my_move]
            if opponent == my_move:
                total_score += 3
            elif win_condition[my_move] == opponent:
                total_score += 6

    print(total_score)

