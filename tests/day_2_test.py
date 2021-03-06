from advent_of_code_2021.day_2 import parse_data, parse_data_2, parse_instructions

TEST_DATA = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""
TEST_DATA = parse_instructions(
    [item.strip().split(" ") for item in TEST_DATA.split("\n")]
)


def test_parse_data():
    assert (15, 10) == parse_data(TEST_DATA)


def test_parse_data_2():
    assert (15, 60) == parse_data_2(TEST_DATA)
