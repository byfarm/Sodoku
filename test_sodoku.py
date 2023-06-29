import game
import pytest


def test_find_sector():
	sec = list(game.find_sec(1, 6))
	print(sec)
	assert len(list(sec)) == 9


def test_main():
	print()
	board = game.main()
	for r in board:
		print(r)
	assert board == [
			[9, 8, 3, 7, 6, 4, 5, 2, 1],
			[2, 6, 7, 1, 5, 8, 9, 4, 3],
			[4, 5, 1, 2, 9, 3, 7, 6, 8],
			[3, 1, 2, 4, 7, 9, 8, 5, 6],
			[5, 7, 8, 6, 1, 2, 4, 3, 9],
			[6, 4, 9, 3, 8, 5, 1, 7, 2],
			[8, 3, 6, 5, 4, 1, 2, 9, 7],
			[7, 9, 4, 8, 2, 6, 3, 1, 5],
			[1, 2, 5, 9, 3, 7, 6, 8, 4]
		]