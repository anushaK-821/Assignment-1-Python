def print_board(board):
    for i in range(0,9,3):
        print('|'.join(board[i:i+3]))
        if i<6:
            print('--+---+---')

board_state=['X ',' O ',' X',
             '  ',' X ',' O',
             'O ','   ',' X']

print("Tic-Tac-Toe Board with X and O:")
print_board(board_state)
        
