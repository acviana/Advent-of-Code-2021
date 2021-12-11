from typing import Dict, List, Tuple


def load_data() -> List[List[str]]:
    with open("inputs/day_2_input.txt") as f:
        return [item.strip().split(" ") for item in f.readlines()]


def translate_instruction_part_1(input_instruction: List[str]) -> Dict:
    instruction = {
        "direction": input_instruction[0],
        "magnitude": int(input_instruction[1]),
    }
    if instruction["direction"] == "up":
        return {"position_change": 0, "depth_change": -1 * instruction["magnitude"]}
    elif instruction["direction"] == "down":
        return {"position_change": 0, "depth_change": instruction["magnitude"]}
    elif instruction["direction"] == "forward":
        return {"position_change": instruction["magnitude"], "depth_change": 0}
    else:
        assert False


def translate_instruction_part_2(input_instruction: List[str]) -> Dict:
    instruction = {
        "direction": input_instruction[0],
        "magnitude": int(input_instruction[1]),
    }
    if instruction["direction"] == "up":
        return {
            "position_change": 0,
            "depth_change": 0,
            "aim_change": -1 * instruction["magnitude"],
        }
    elif instruction["direction"] == "down":
        return {
            "position_change": 0,
            "depth_change": 0,
            "aim_change": instruction["magnitude"],
        }
    elif instruction["direction"] == "forward":
        return {
            "position_change": instruction["magnitude"],
            "depth_change_multiple": instruction["magnitude"],
            "aim_change": 0,
        }
    else:
        assert False


def parse_data(data: List[List[str]]) -> Tuple[int, int]:
    instruction_list = [translate_instruction_part_1(item) for item in data]
    return (
        sum([item["position_change"] for item in instruction_list]),
        sum([item["depth_change"] for item in instruction_list]),
    )


def parse_data_2(data: List[List[str]]) -> Tuple[int, int]:
    instruction_list = [translate_instruction_part_2(item) for item in data]
    coordinate_dict = {"position": 0, "depth": 0, "aim": 0}
    for instruction in instruction_list:
        if instruction["aim_change"] != 0:
            coordinate_dict["aim"] += instruction["aim_change"]
        else:
            coordinate_dict["position"] += instruction["position_change"]
            coordinate_dict["depth"] += (
                instruction["depth_change_multiple"] * coordinate_dict["aim"]
            )
    return (coordinate_dict["position"], coordinate_dict["depth"])


def main() -> None:
    data = load_data()
    position = parse_data(data)
    print(f"Position is {position}")
    print(f"Answer in {position[0] * position[1]}")
    position = parse_data_2(data)
    print(f"Position is {position}")
    print(f"Answer in {position[0] * position[1]}")


if __name__ == "__main__":
    main()
