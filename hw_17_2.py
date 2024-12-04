"""
tic tac toe
"""

def print_board(board):
    """
    Отображает текущее состояние игрового поля
    """
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")

def check_winner(board):
    """
    Проверяет наличие победителя на игровом поле
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def tic_tac_toe():
    """
    Запускает игру Крестики-нолики
    """
    board = [[str(i) for i in range(1, 4)],
             [str(i) for i in range(4, 7)],
             [str(i) for i in range(7, 10)]]
    current_player = "X"
    moves = 0

    print("********** Игра Крестики-нолики**********")

    while moves < 9:
        print_board(board)
        move = int(input(f"Куда поставим {current_player}? ")) - 1

        if move < 0 or move >= 9:
            print("Пожалуйста, введите число от 1 до 9!")
            continue

        row = move // 3
        column = move % 3

        if board[row][column] not in ("X", "O"):
            board[row][column] = current_player
            moves += 1

            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Игрок {winner} победил!")
                return

            current_player = "O" if current_player == "X" else "X"
        else:
            print("Эта клетка уже занята, выберите другую!")

    print_board(board)
    print("Игра закончилась вничью!")

if __name__ == "__main__":
    tic_tac_toe()
