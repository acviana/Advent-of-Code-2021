from advent_of_code_2021.day_2 import parse_data

TEST_DATA = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""
TEST_DATA = [item.strip().split(" ") for item in TEST_DATA.split("\n")]


def test_parse_data():
    assert (15, 10) == parse_data(TEST_DATA)
