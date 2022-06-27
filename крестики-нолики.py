print('    Добро пожаловать в игру    ')
print('       крестики-нолики!        ')
print('-------------------------------')
print('     крестик ходит первым!     ')
print('  для хода введите номер строки')
print('      затем номер столбца      ')
print(' ')

field = [[' '] * 3 for i in range(3)]

def game_field():
    print('   | 0 | 1 | 2 |')
    print('________________')
    for i, row  in enumerate(field):
        info_row = f" {i} | {' | '.join(row)} |"
        print(info_row)
        print('________________')

def ask():
    while True:
        x = input('введите номер строки для хода - ')
        y = input('введите номер столбца для хода - ')
        try:
            x, y = int(x), int(y)
        except ValueError:
            print('Некорректный ввод. Повторите')
            continue
        if 0 <= x <= 2 and 0 <= y <= 2:
            if field[x][y] == ' ':
                return x, y
                break
            else:
                print('Клетка занята! Повторите ввод')
        else:
            print('Координаты вне диапазона. Повторите ввод')

def check_win():
    if any([field[0][0] == field[0][1] == field[0][2] != ' ',
            field[1][0] == field[1][1] == field[1][2] != ' ',
            field[2][0] == field[2][1] == field[2][2] != ' ',
            field[0][0] == field[1][0] == field[2][0] != ' ',
            field[0][1] == field[1][1] == field[2][1] != ' ',
            field[0][2] == field[1][2] == field[2][2] != ' ',
            field[0][0] == field[1][1] == field[2][2] != ' ',
            field[0][2] == field[1][1] == field[2][0] != ' ']):
        return True
    else:
        return False

num = 0
while True:
    game_field()
    print('ходит крестик')
    x, y = ask()
    field[x][y] = 'X'
    num += 1
    game_field()
    if check_win():
        print('Поздравляю! Выиграл КРЕСТИК!')
        break
    if num >= 9:
        print('Ничья!')
        break
    print('ходит нолик')
    x, y = ask()
    field[x][y] = '0'
    if check_win():
        game_field()
        print('Поздравляю! Выиграл НОЛИК!')
        break
    num += 1