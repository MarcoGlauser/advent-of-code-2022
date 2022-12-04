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
            opponent, outcome = line.strip().split(' ')
            if outcome == 'X':  # lose
                my_move = win_condition[opponent]
            if outcome == 'Y':  # draw
                my_move = opponent
                total_score += 3
            if outcome == 'Z':  # win
                difference = score.keys() ^ {opponent, win_condition[opponent]}
                my_move = difference.pop()
                total_score += 6

            total_score += score[my_move]

    print(total_score)

