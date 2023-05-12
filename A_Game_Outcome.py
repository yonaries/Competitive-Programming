def game_outcome(n, board):
    winning_squares = 0

    for i in range(n):
        for j in range(n):
            row_sum = sum(board[i])
            col_sum = sum(board[k][j] for k in range(n))

            if col_sum > row_sum:
                winning_squares += 1

    return winning_squares


if __name__ == '__main__':
    n = int(input())
    board = []
    for i in range(n):
        board.append([int(x) for x in input().split()])
    print(game_outcome(n, board))
