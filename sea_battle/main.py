import random

def create_board():
    board = [[' ' for _ in range(10)] for _ in range(10)]
    return board

def print_board(board, show_damaged_only=False, player_shots=None):
    print("  А Б В Г Д Е Ж З И К")
    for i, row in enumerate(board):
        row_display = []
        for j, cell in enumerate(row):
            if show_damaged_only and player_shots and (i, j) not in player_shots:
                row_display.append(' ')
            else:
                row_display.append(cell)
        print(i, ' '.join(row_display))

def place_ship(board, ship_size):
    orientation = random.choice(['горизонтальный', 'вертикальный'])
    if orientation == 'горизонтальный':
        row = random.randint(0, 9)
        col = random.randint(0, 10 - ship_size)
        for i in range(ship_size):
            if board[row][col + i] != ' ':
                return place_ship(board, ship_size)
        for i in range(ship_size):
            board[row][col + i] = 'O'
    else:
        row = random.randint(0, 10 - ship_size)
        col = random.randint(0, 9)
        for i in range(ship_size):
            if board[row + i][col] != ' ':
                return place_ship(board, ship_size)
        for i in range(ship_size):
            board[row + i][col] = 'O'
    return board

def is_valid_input(input_str):
    if len(input_str) != 2:
        return False
    col, row = input_str[0], input_str[1]
    return col.isalpha() and col.upper() in 'АБВГДЕЖЗИК' and row.isdigit() and 0 <= int(row) <= 9

def get_user_input():
    while True:
        user_input = input("Введите координаты выстрела (например, А3): ").upper()
        if is_valid_input(user_input):
            return user_input
        else:
            print("Некорректный ввод. Пожалуйста, введите координаты в формате А3.")

def convert_input(input_str):
    col, row = input_str[0], input_str[1]
    col_num = ord(col) - ord('А')
    row_num = int(row)
    return row_num, col_num

def play_battleship():
    player_board = create_board()
    computer_board = create_board()
    player_shots = set()
    computer_shots = set()

    for ship_size in [5, 4, 3, 3, 2]:
        player_board = place_ship(player_board, ship_size)
        computer_board = place_ship(computer_board, ship_size)

    while True:
        print("Ваша доска:")
        print_board(player_board)
        print("\nДоска противника:")
        print_board(computer_board, show_damaged_only=True, player_shots=computer_shots)

        # Ход игрока
        user_input = get_user_input()
        row, col = convert_input(user_input)

        if (row, col) in player_shots:
            print("Вы уже стреляли в эту клетку. Попробуйте еще раз.")
            continue

        player_shots.add((row, col))

        if computer_board[row][col] == 'O':
            print("Попадание!")
            computer_board[row][col] = 'X'
            computer_shots.add((row, col))
        else:
            print("Промах!")

        if all('O' not in row for row in computer_board):
            print("Вы выиграли!")
            break

if __name__ == "__main__":
    play_battleship()
