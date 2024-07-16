def print_board(board):
    print("Current board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        try:
            row, col = map(int, input(f"Player {current_player}, enter your move (row and column): ").split())
        except ValueError:
            print("Invalid input. Please enter row and column as two numbers separated by a space.")
            continue

        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != ' ':
            print("Invalid move. Try again.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("The game is a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
