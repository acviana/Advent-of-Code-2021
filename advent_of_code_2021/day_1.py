from typing import List


def load_data() -> List[int]:
    with open("inputs/day_1_input.txt") as f:
        return [int(item.strip()) for item in f.readlines()]


def parse_data(data: List[int]) -> List[bool]:
    return [True if data[i] > data[i - 1] else False for i in range(1, len(data))]


def main() -> None:
    data = load_data()
    print(f"Length of data: {len(data)}")
    result = parse_data(data)
    print(f"Length of result: {len(result)}")
    print(f"Solution: {sum(result)}")


if __name__ == "__main__":
    main()
