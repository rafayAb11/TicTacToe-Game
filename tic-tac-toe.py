board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for i in range(len(board)):
        print(" | ".join(board[i]))
        if i<len(board)-1:
            print("--+---+--")

print_board(board)

def player_move(board,player):
    while True:
        try:
            row = int(input(f"Player{player}, enter row(0-2): "))
            col = int(input(f"Player {player}, enter column(0-2): "))

            if board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("Cell already taken")
        except (ValueError, IndexError):
            print("Invalid input!")

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
        
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
        
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    for turn in range(9):
        print_board(board)
        player_move(board, current_player)

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return

        current_player = 'O' if current_player == 'X' else 'X' 

    print_board(board)
    print("Its a draw!")

play_game()