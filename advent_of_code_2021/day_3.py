from collections import Counter
from typing import List


def load_data() -> List[str]:
    with open("inputs/day_3_input.txt") as f:
        return [item.strip() for item in f.readlines()]


def get_common_value(
    data: List[str],
    column_index: int,
    return_most_common_value: bool = True,
) -> str:
    counter = Counter([item[column_index] for item in data])
    if return_most_common_value:
        return "1" if counter["1"] == counter["0"] else counter.most_common()[0][0]
    else:
        return "0" if counter["1"] == counter["0"] else counter.most_common()[1][0]


def parse_data_part_1(data: List[str]) -> str:
    binary_register = ""
    for column_index in range(0, len(data[0])):
        binary_register += get_common_value(
            data, column_index, return_most_common_value=True
        )
    return binary_register


def recursive_sieve(
    data: List[str],
    column_index: int,
    return_most_common_value: bool = False,
    verbose: bool = False,
):
    most_common_value = get_common_value(
        data,
        column_index,
        return_most_common_value=return_most_common_value,
    )
    result = [item for item in data if item[column_index] == most_common_value]
    if len(result) == 1:
        return result[0]
    else:
        if verbose:
            print(f"Remaining Rows: {len(result)}")
        return recursive_sieve(
            result,
            column_index + 1,
            return_most_common_value=return_most_common_value,
            verbose=verbose,
        )


def run_part_1(data) -> None:
    # Create both binary registers
    binary_register = parse_data_part_1(data)
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


def run_part_2(data) -> None:

    # Calculate the Oxygen Register Rating in base 10
    oxygen_generator_rating = recursive_sieve(
        data, 0, return_most_common_value=True, verbose=True
    )
    print(f"Oxygen generator rating in binary is {oxygen_generator_rating}")
    oxygen_generator_rating = int(oxygen_generator_rating, 2)
    print(f"Oxygen generator rating in decimal is {oxygen_generator_rating}")

    # Calculate the C02 Scrubber Rating in base 10
    co2_scrubber_rating = recursive_sieve(
        data, 0, return_most_common_value=False, verbose=True
    )
    print(f"CO2 scrubber rating in binary is {co2_scrubber_rating}")
    co2_scrubber_rating = int(co2_scrubber_rating, 2)
    print(f"CO2 scrubber rating in decimal is {co2_scrubber_rating}")

    # Calculate the final product in base 10
    print(f"Answer is {oxygen_generator_rating * co2_scrubber_rating}")


def main() -> None:

    # Load the data
    data = load_data()
    print(f"Loaded {len(data)} rows and {len(data[0])} columns")

    print("Part 1")
    run_part_1(data)

    print("Part 2")
    run_part_2(data)


if __name__ == "__main__":
    main()
