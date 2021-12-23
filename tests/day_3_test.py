from advent_of_code_2021.day_3 import (
    get_common_value,
    parse_data_part_1,
    recursive_sieve,
)

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


def test_parse_data_part_1():
    assert parse_data_part_1(TEST_DATA) == "10110"


def test_get_common_value():
    data = ["0", "1"]
    assert get_common_value(data, 0, return_most_common_value=True) == "1"
    assert get_common_value(data, 0, return_most_common_value=False) == "0"


def test_recursive_sieve():
    assert (
        recursive_sieve(TEST_DATA, 0, return_most_common_value=True, verbose=False)
        == "10111"
    )
    assert (
        recursive_sieve(TEST_DATA, 0, return_most_common_value=False, verbose=False)
        == "01010"
    )
