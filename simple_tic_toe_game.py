# Simple Tic-Tac-Toe in Python

board = [" " for _ in range(9)]

def print_board():
    for i in range(3):
        print("  |  ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("---------------")

def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]            # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def game():
    current_player = "X"
    for turn in range(9):
        print_board()
        move = int(input(f"Player {current_player}, choose your move (0-8): "))
        if board[move] != " ":
            print("Invalid move. Try again.")
            continue
        board[move] = current_player
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            return
        current_player = "O" if current_player == "X" else "X"
    print_board()
    print("It's a draw!")

game()
