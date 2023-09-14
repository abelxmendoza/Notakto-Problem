def print_board(board):
    return f"{board[0]:^3} | {board[1]:^3} | {board[2]:^3}\n{'-' * 13}\n{board[3]:^3} | {board[4]:^3} | {board[5]:^3}\n{'-' * 13}\n{board[6]:^3} | {board[7]:^3} | {board[8]:^3}\n"

def switch_player(player):
    return 'X' if player == 'O' else 'O'

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if (board[i] == board[i + 3] == board[i + 6] == player) or \
           (board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] == player):
            return True
    if (board[0] == board[4] == board[8] == player) or \
       (board[2] == board[4] == board[6] == player):
        return True
    return False

def evaluate_board(board, player):
    # Check for a win or a draw
    if check_win(board, player):
        return 1  # Win
    elif ' ' not in board:
        return 0  # Draw
    else:
        return -1  # Loss

def main():
    initial_board = [' ', 'X', 'X', ' ', 'O', ' ', ' ', 'X', ' ']
    player = 'O'  # Start with player O
    
    print("Initial board:")
    print(print_board(initial_board))
    
    for depth in range(2):
        print(f"Depth {depth + 1}, Player {player}'s turn:")
        
        for i in range(9):
            if initial_board[i] == ' ':
                board_copy = initial_board.copy()
                board_copy[i] = player
                evaluation = evaluate_board(board_copy, player)
                if evaluation == -1:
                    print(f"Move {i + 1} -\n{print_board(board_copy)} - Loss (Heuristic)\n")
                elif evaluation == 0:
                    print(f"Move {i + 1} -\n{print_board(board_copy)} - Draw (Heuristic)\n")
                elif evaluation == 1:
                    print(f"Move {i + 1} -\n{print_board(board_copy)} - Win (Terminal State)\n")
        
        player = switch_player(player)

if __name__ == "__main__":
    main()
