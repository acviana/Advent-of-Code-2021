from typing import List, Tuple


def load_data() -> List[List[str]]:
    with open("inputs/day_2_input.txt") as f:
        return [item.strip().split(" ") for item in f.readlines()]


def translate_instruction(instruction: List[str]) -> Tuple[int, int]:
    if instruction[0] == "up":
        return (0, -1 * int(instruction[1]))
    elif instruction[0] == "down":
        return (0, int(instruction[1]))
    elif instruction[0] == "forward":
        return (int(instruction[1]), 0)
    else:
        assert False


def parse_data(data: List[List[str]]) -> Tuple[int, int]:
    instruction_list = [translate_instruction(item) for item in data]
    return (
        sum([item[0] for item in instruction_list]),
        sum([item[1] for item in instruction_list]),
    )


def main() -> None:
    data = load_data()
    position = parse_data(data)
    print(f"Position is {position}")
    print(f"Answer in {position[0] * position[1]}")


if __name__ == "__main__":
    main()
