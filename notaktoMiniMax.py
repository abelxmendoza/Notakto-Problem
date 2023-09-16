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

def minimax(board, depth, player):
    if depth == 0 or evaluate_board(board, player) != -1:
        # If at depth 0 or terminal state, return the evaluation
        return evaluate_board(board, player)
    
    if player == 'X':
        max_eval = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board_copy = board.copy()
                board_copy[i] = player
                print(f"Minimax at Depth {depth}, Player {player}, Move {i + 1} -\n{print_board(board_copy)}")
                eval = minimax(board_copy, depth - 1, switch_player(player))
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board_copy = board.copy()
                board_copy[i] = player
                print(f"Minimax at Depth {depth}, Player {player}, Move {i + 1} -\n{print_board(board_copy)}")
                eval = minimax(board_copy, depth - 1, switch_player(player))
                min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board, player):
    best_move = -1
    best_eval = -float('inf') if player == 'X' else float('inf')
    
    for i in range(9):
        if board[i] == ' ':
            board_copy = board.copy()
            board_copy[i] = player
            eval = minimax(board_copy, 1, switch_player(player))
            
            if player == 'X' and eval > best_eval:
                best_eval = eval
                best_move = i
            elif player == 'O' and eval < best_eval:
                best_eval = eval
                best_move = i
    
    return best_move

def main():
    initial_board = [' ', 'X', 'X', ' ', 'O', ' ', ' ', 'X', ' ']
    player = 'O'  # Start with player O
    
    print("Initial board:")
    print(print_board(initial_board))
    
    # Find the best starting move using minimax
    best_starting_move = find_best_move(initial_board, player)
    
    print(f"Best starting move for Player {player}: Move {best_starting_move + 1}")
    
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
    
    print("Minimax calculations are done on the board to choose the best starting move.")

if __name__ == "__main__":
    main()

