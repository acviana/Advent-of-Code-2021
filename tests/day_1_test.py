from advent_of_code_2021.day_1 import parse_data, window_sum

TEST_DATA = """199
200
208
210
200
207
240
269
260
263"""
TEST_DATA = [int(item) for item in TEST_DATA.split("\n")]

EXPECTED_TEST_RESULT = [True, True, True, False, True, True, True, False, True]


def test_parse_data():
    result = parse_data(TEST_DATA)
    assert result == EXPECTED_TEST_RESULT
    assert len(result) == len(TEST_DATA) - 1
    assert sum(result) == 7


TEST_WINDOW_SUM_RESULT = [607, 618, 618, 617, 647, 716, 769, 792]


def test_window_data():
    result = window_sum(TEST_DATA)
    assert result == TEST_WINDOW_SUM_RESULT
