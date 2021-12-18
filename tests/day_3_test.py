from advent_of_code_2021.day_3 import parse_data

TEST_DATA = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""
TEST_DATA = [item for item in TEST_DATA.split()]


def test_parse_data():
    assert parse_data(TEST_DATA, 5, 12) == "10110"
