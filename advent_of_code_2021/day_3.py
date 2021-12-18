from typing import List


def load_data() -> List[str]:
    with open("inputs/day_3_input.txt") as f:
        return [item.strip() for item in f.readlines()]


def sum_column(data: List[str], column: int) -> int:
    return sum([int(item[column]) for item in data])


def parse_data(
    data: List[str], column_count: int, row_count: int, verbose=False
) -> str:
    binary_register = ""
    for column in range(0, column_count):
        column_sum = sum_column(data, column)
        binary = "1" if column_sum > (row_count / 2) else "0"
        if verbose:
            print(f"column_sum is {column_sum} and binary value is {binary}")
        binary_register += binary
    return binary_register


def main() -> None:

    # Load the data
    data = load_data()
    row_count = len(data)
    column_count = len(data[0])
    print(f"Loaded {row_count} rows and {column_count} columns")

    # Create both binary registers
    binary_register = parse_data(data, column_count, row_count, verbose=True)
    print(f"binary_register is {binary_register}")
    binary_complement = "".join(
        ["0" if item == "1" else "1" for item in binary_register]
    )
    print(f"binary_complement is {binary_complement}")

    # Transform binary registers into base 10
    gamma = int(binary_register, 2)
    print(f"Base 10 of binary_register is {gamma}")
    epsilon = int(binary_complement, 2)
    print(f"Base 10 of binary_complement is {epsilon}")

    # Calculate the final product in base 10
    print(f"Product of gamma and delta is {gamma * epsilon}")


if __name__ == "__main__":
    main()
