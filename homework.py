list_numbers = list(range(1, 10))

victories = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6, 9)]


def game_board():
    print('---------')
    for i in range(3):
        print('|', list_numbers[0 + i * 3], list_numbers[1 + i * 3], list_numbers[2 + i * 3], '|')
        print('---------')


def take_input(game_progress):
    while True:
        value = input("В какую ячейку поставить: " + game_progress + " ? - ")
        if not (value in "123456789"):
            print("Вы ввели не верный символ, повторите!")
            continue
        value = int(value)
        if str(list_numbers[value - 1]) in "XO":
            print("Эта клетка больше не используется!")
            continue
        list_numbers[value - 1] = game_progress
        break


def check_win():
    for each in victories:
        if (list_numbers[each[0] - 1]) == (list_numbers[each[1] - 1]) == (list_numbers[each[2] - 1]):
            return list_numbers[each[1] - 1]
    else:
        return False


def main():
    stroke_numbers = 0
    while True:
        game_board()
        if stroke_numbers % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        if stroke_numbers > 3:
            winner = check_win()
            if winner:
                game_board()
                print(winner, "победил!")
                break
        stroke_numbers += 1
        if stroke_numbers == 9:
            game_board()
            print("Ничья!")
            break


main()
