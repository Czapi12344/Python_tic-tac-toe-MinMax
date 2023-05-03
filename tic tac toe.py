def print_board(board):
    print("  1 2 3")
    for i in range(3):
        row = str(i + 1) + " "
        for j in range(3):
            row += board[i][j] + " "
        print(row)


def get_player_move(board):
    while True:
        row = int(input("Enter row (1-3): ")) - 1
        col = int(input("Enter column (1-3): ")) - 1
        if board[row][col] == " ":
            return row, col
        print("That cell is already taken. Try again.")


def get_computer_move(board):
    best_score = float('-inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move


def minimax(board, maximizing_player):
    if is_game_over(board):
        winner = get_winner(board)
        if winner == "O":
            return 1
        elif winner == "X":
            return -1
        else:
            return 0
    if maximizing_player:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score


def is_game_over(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        elif board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    elif board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    elif " " not in board[0] and " " not in board[1] and " " not in board[2]:
        return True
    return False


def get_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        elif board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)
    player_turn = True
    while not is_game_over(board):
        if player_turn:
            row, col = get_player_move(board)
            board[row][col] = "X"
        else:
            row, col = get_computer_move(board)
            board[row][col] = "O"
            print("Computer plays:")
        print_board(board)
        player_turn = not player_turn
    winner = get_winner(board)
    if winner:
        print(f"{winner} wins!")
    else:
        print("It's a tie.")


play_game()
