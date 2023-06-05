from random import randint as ri


def rnd_positions(board_size: int) -> list[tuple[int, int]]:
    result = []
    while len(result) != board_size:
        applicant = (ri(1, board_size), ri(1, board_size))
        if applicant not in result:
            result.append(applicant)
    return result


def is_desk_validate(positions: list[tuple[int, int]], board_size: int) -> bool:
    cur_positions = []
    for position in positions:
        if position in cur_positions or not 1 <= position[0] <= board_size or not 1 <= position[1] <= board_size:
            return False
        cur_positions.append(position)
    if len(cur_positions) != board_size:
        return False

    board = [[0 for _ in range(board_size)] for _ in range(board_size)]
    for position in cur_positions:
        board[position[0] - 1][position[1] - 1] = 1

    for row in board:
        if sum(row) > 1:
            return False

    for column in range(board_size):
        summ = 0
        for row in range(board_size):
            summ += board[row][column]
            if summ > 1:
                return False

    for i in range(board_size):
        summ_up_main = 0
        summ_down_main = 0
        summ_up_secondary = 0
        summ_down_secondary = 0
        for j in range(i + 1):
            summ_up_main += board[j][board_size - 1 - i + j]
            summ_down_main += board[board_size - 1 - i + j][j]
            summ_up_secondary += board[j][i - j]
            summ_down_secondary += board[board_size - 1 - i + j][board_size - 1 - j]

        if summ_up_main > 1 or summ_down_main > 1 or summ_up_secondary > 1 or summ_down_secondary > 1:
            return False

    return True


if __name__ == '__main__':
    size_board = 8
    count = 0
    while count != 4:
        pos = rnd_positions(size_board)
        if is_desk_validate(pos, size_board):
            print(pos)
            count += 1
