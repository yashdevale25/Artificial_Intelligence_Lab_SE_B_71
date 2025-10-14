import math

PLAYER = 'X'   # AI - MAX
OPPONENT = 'O' # Human - MIN
EMPTY = '_'

def create_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)]

def print_board(board):
    print("\nCurrent Board:")
    for row in board:
        print(' '.join(row))
    print()

def is_moves_left(board):
    for row in board:
        if EMPTY in row:
            return True
    return False

def evaluate(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return +1 if board[i][0] == PLAYER else -1
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return +1 if board[0][i] == PLAYER else -1
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return +1 if board[0][0] == PLAYER else -1
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return +1 if board[0][2] == PLAYER else -1
    return 0

def minimax(board, depth, is_max):
    score = evaluate(board)
    if score == 1 or score == -1:
        return score
    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = EMPTY
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = OPPONENT
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = EMPTY
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER
                move_val = minimax(board, 0, False)
                board[i][j] = EMPTY

                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
    return best_move

def play_game():
    board = create_board()
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O', AI is 'X'.")
    print("Enter your move (0-8) as per the board positions:")
    print("0 | 1 | 2")
    print("---------")
    print("3 | 4 | 5")
    print("---------")
    print("6 | 7 | 8")
    print_board(board)

    while True:
        # Human move
        while True:
            try:
                move = int(input("Your move (0-8): "))
                if move < 0 or move > 8:
                    print("Invalid input, number must be between 0 and 8.")
                    continue
                row, col = divmod(move, 3)
                if board[row][col] == EMPTY:
                    board[row][col] = OPPONENT
                    break
                else:
                    print("Cell already taken. Try another move.")
            except ValueError:
                print("Invalid input. Please enter an integer between 0 and 8.")

        print_board(board)

        if evaluate(board) == -1:
            print(" You win!")
            break
        if not is_moves_left(board):
            print(" It's a draw!")
            break

        # AI move
        print("AI is making a move...")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = PLAYER
        print_board(board)

        if evaluate(board) == 1:
            print(" AI wins!")
            break
        if not is_moves_left(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()

