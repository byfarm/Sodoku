import copy


def solve_sodoku(board: list[list]):
	find = find_e(board)
	if not find:
		return True
	else:
		r, c = find

	for inp in range(1, 10):
		tandf = valid(board, inp, (r, c))
		if tandf:
			board[r][c] = inp

			if solve_sodoku(board):
				return True

			board[r][c] = 0

	return False


def valid(board, num, pos: tuple):
	r, c = pos[0], pos[1]
	ess_spac = find_spaces(board, r, c)
	if num in ess_spac:
		return False
	else:
		return True


def find_e(board):
	# go through each row and column
	for r in range(9):
		for c in range(9):
			# find the interested space, if 0 then it is empty
			space = board[r][c]
			if space == 0:
				return (r, c)
	return None


def find_sec(row: int, column: int):
	sector = []
	for r in range(1, 4):
		if row < 3 * r:
			r_val = list(range((r - 1) * 3, r * 3))
			if column < 3:
				for q in r_val:
					for p in range(3):
						sector.append((q, p))
				break
			elif column < 6:
				for q in r_val:
					for p in range(3, 6):
						sector.append((q, p))
				break

			else:
				for q in r_val:
					for p in range(6, 9):
						sector.append((q, p))
				break
	return sector


def find_spaces(board: list, r: int, c: int):
	row = copy.deepcopy(board[r])
	row.pop(c)
	colum = [board[i][c] for i in range(9)]
	colum.pop(r)
	sector = find_sec(r, c)
	sector.remove((r, c))
	sector_vals = [board[idx[0]][idx[1]] for idx in sector]
	return row + colum + sector_vals


def main():
	board = [
			[0, 0, 0, 0, 0, 4, 0, 0, 1],
			[2, 6, 7, 0, 5, 8, 9, 0, 0],
			[0, 5, 1, 2, 0, 0, 7, 0, 0],
			[3, 1, 0, 0, 0, 0, 8, 5, 0],
			[0, 0, 0, 6, 0, 2, 4, 3, 9],
			[6, 0, 0, 0, 8, 0, 0, 0, 0],
			[8, 3, 6, 5, 4, 1, 2, 9, 0],
			[7, 0, 4, 0, 0, 0, 3, 1, 0],
			[0, 2, 0, 9, 0, 7, 0, 0, 0]
		]
	solve_sodoku(board)
	return board
