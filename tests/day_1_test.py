from advent_of_code_2021.day_1 import parse_data

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

EXPECTED_RESULT = [True, True, True, False, True, True, True, False, True]


def test_parse_data():
    result = parse_data(TEST_DATA)
    assert result == EXPECTED_RESULT
    assert len(result) == len(TEST_DATA) - 1
    assert sum(result) == 7
