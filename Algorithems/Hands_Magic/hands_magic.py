# ID решения 83702600
def data_input():
    press = int(input()) * 2
    matrix_game = ''.join([input() for _ in range(4)])
    return press, matrix_game


def printing_simulator(press:int, matrix_game:str):
    numbers = []
    score = 0
    for score_number in range(1, 10):
        count = matrix_game.count(str(score_number))
        numbers.append(count)

    for score_number in range(9):
        if ((int(numbers[score_number])) <= press
            and int(numbers[score_number] != 0
                 )):
            score += 1
    return score


if __name__ == '__main__':
    press, matrix_game = data_input()
    print(printing_simulator(press,matrix_game))
