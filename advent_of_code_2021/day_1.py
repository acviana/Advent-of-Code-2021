from typing import List


def load_data() -> List[int]:
    with open("inputs/day_1_input.txt") as f:
        return [int(item.strip()) for item in f.readlines()]


def parse_data(data: List[int]) -> List[bool]:
    return [True if data[i] > data[i - 1] else False for i in range(1, len(data))]


def window_sum(data: List[int]) -> List[int]:
    return [sum(data[i : i + 3]) for i in range(0, len(data) - 2)]


def main() -> None:
    data = load_data()
    print("Part 1")
    print(f"Length of data: {len(data)}")
    result = parse_data(data)
    print(f"Length of result: {len(result)}")
    print(f"Solution: {sum(result)}")

    print("Part 2")
    print(f"Length of data: {len(data)}")
    windowed_data = window_sum(data)
    print(f"Length of windowed data: {len(windowed_data)}")
    print(f"Solution: {sum(parse_data(windowed_data))}")


if __name__ == "__main__":
    main()
