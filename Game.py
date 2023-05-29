# Создаем пустую доску 3x3 для игры
board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]

# Функция, которая выводит текущее состояние доски
def display_board():
    print(board[0][0] + '|' + board[0][1] + '|' + board[0][2])
    print(board[1][0] + '|' + board[1][1] + '|' + board[1][2])
    print(board[2][0] + '|' + board[2][1] + '|' + board[2][2])

# Функция, которая проверяет, выиграл ли игрок с помощью заданного символа (X или O)
def check_win(symbol):
    # Проверяем все возможные комбинации для выигрыша
    if ((board[0][0] == symbol and board[0][1] == symbol and board[0][2] == symbol) or
        (board[1][0] == symbol and board[1][1] == symbol and board[1][2] == symbol) or
        (board[2][0] == symbol and board[2][1] == symbol and board[2][2] == symbol) or
        (board[0][0] == symbol and board[1][0] == symbol and board[2][0] == symbol) or
        (board[0][1] == symbol and board[1][1] == symbol and board[2][1] == symbol) or
        (board[0][2] == symbol and board[1][2] == symbol and board[2][2] == symbol) or
        (board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol) or
        (board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol)):
        return True
    else:
        return False

# Функция, которая проверяет, что клетка свободна для хода
def is_valid_move(row, col):
    if board[row][col] == '-':
        return True
    else:
        return False

# Функция, которая запрашивает у пользователя координаты хода
def get_move(symbol):
    print("Ход игрока " + symbol)
    row = int(input("Введите номер строки: "))
    col = int(input("Введите номер столбца: "))

    # Проверяем, валидный ли ход
    if not is_valid_move(row, col):
        print("Клетка занята или неверные координаты. Попробуйте еще раз.")
        get_move(symbol)

    return row, col

# Основной цикл игры
def play_game():
    # Выводим начальное состояние доски
    display_board()
    # Игрок X начинает
    current_player = 'X'
    # Цикл продолжается до тех пор, пока нет победителя или не закончатся свободные клетки
    while True:
        row, col = get_move(current_player)
        board[row][col] = current_player
        display_board()
        # Проверяем, выиграл ли текущий игрок
        if check_win(current_player):
            print("Игрок " + current_player + " победил!")
            break
        # Если свободных клеток больше нет, то ничья
        if all('-' not in sublist for sublist in board):
            print("Ничья!")
            break
        # Меняем игрока после каждого хода
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

# Запускаем игру
play_game()