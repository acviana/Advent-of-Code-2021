from advent_of_code_2021.day_4 import Board, parse_data, run_game

TEST_DATA = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""
TEST_DATA = [item.strip() for item in TEST_DATA.split("\n")]

EXPECTED_TEST_RESULT = {
    "numbers": [
        7,
        4,
        9,
        5,
        11,
        17,
        23,
        2,
        0,
        14,
        21,
        24,
        10,
        16,
        13,
        6,
        15,
        25,
        12,
        22,
        18,
        20,
        8,
        19,
        3,
        26,
        1,
    ],
    "boards": [
        [
            [22, 13, 17, 11, 0],
            [8, 2, 23, 4, 24],
            [21, 9, 14, 16, 7],
            [6, 10, 3, 18, 5],
            [1, 12, 20, 15, 19],
        ],
        [
            [3, 15, 0, 2, 22],
            [9, 18, 13, 17, 5],
            [19, 8, 7, 25, 23],
            [20, 11, 10, 24, 4],
            [14, 21, 16, 12, 6],
        ],
        [
            [14, 21, 17, 24, 4],
            [10, 16, 15, 9, 19],
            [18, 8, 23, 26, 20],
            [22, 11, 13, 6, 5],
            [2, 0, 12, 3, 7],
        ],
    ],
}


def test_parse_data():
    result = parse_data(TEST_DATA)
    assert result["numbers"] == EXPECTED_TEST_RESULT["numbers"]
    assert len(result["boards"]) == len(EXPECTED_TEST_RESULT["boards"])
    for result_board, expected_board in zip(
        result["boards"], EXPECTED_TEST_RESULT["boards"]
    ):
        assert result_board == expected_board
    assert result == EXPECTED_TEST_RESULT


def test_board_pick_number():
    board = Board(parse_data(TEST_DATA)["boards"][0])
    assert board.board[(0, 0)]["picked"] is False
    board.pick_number(22)
    assert board.board[(0, 0)]["picked"] is True


def test_board_is_winner():
    result = parse_data(TEST_DATA)
    board = Board(parse_data(TEST_DATA)["boards"][2])
    assert board.is_winner is False
    for number in result["numbers"]:
        board.pick_number(number)
        if number != 24:
            assert board.is_winner is False
        else:
            assert board.is_winner is True
            break


def test_board_unmarked_sum():
    result = parse_data(TEST_DATA)
    board = Board(parse_data(TEST_DATA)["boards"][2])
    for number in result["numbers"]:
        board.pick_number(number)
        if number == 24:
            assert board.is_winner is True
            assert board.unmarked_sum == 188
            break


def test_run_game_to_win():
    parsed_data = parse_data(TEST_DATA)
    game_winner = run_game(parsed_data, play_to_win=True)
    assert game_winner["number"] == 24
    assert game_winner["unmarked_sum"] == 188


def test_run_game_to_lose():
    parsed_data = parse_data(TEST_DATA)
    game_winner = run_game(parsed_data, play_to_win=False)
    assert game_winner["number"] == 13
    assert game_winner["unmarked_sum"] == 148
