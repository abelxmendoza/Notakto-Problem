def print_board(board):
    return f"{board[0]} | {board[1]} | {board[2]}\n---------\n{board[3]} | {board[4]} | {board[5]}\n---------\n{board[6]} | {board[7]} | {board[8]}\n"

def switch_player(player):
    return 'X' if player == 'O' else 'O'

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
                print(print_board(board_copy))
        
        player = switch_player(player)

if __name__ == "__main__":
    main()
