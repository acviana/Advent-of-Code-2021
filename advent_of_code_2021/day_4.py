def load_data() -> list[str]:
    with open("inputs/day_4_input.txt") as f:
        return [item.strip() for item in f.readlines()]


def parse_data(data: list[str]) -> dict:
    output: dict[str, list] = {
        "numbers": [],
        "boards": [],
    }

    output["numbers"] = [int(item) for item in data[0].split(",")]

    temp_board: list = []
    for row in data[2:]:
        if row == "":
            output["boards"] += [temp_board]
            temp_board = []
        else:
            temp_board += [[int(item) for item in row.split()]]
    output["boards"] += [temp_board]

    return output


class Board:
    def __init__(self, input):
        self._input = input
        self._load_board()

    def _load_board(self) -> None:
        board = {}
        for row_index in range(0, 5):
            for column_index in range(0, 5):
                board[(column_index, row_index)] = {
                    "number": self._input[column_index][row_index],
                    "picked": False,
                }
        self.board = board

    def _is_winner(self) -> bool:
        for column_index in range(0, 5):
            column_sum = 0
            for row_index in range(0, 5):
                column_sum += self.board[(column_index, row_index)]["picked"]
            if column_sum == 5:
                return True

        for row_index in range(0, 5):
            row_sum = 0
            for column_index in range(0, 5):
                row_sum += self.board[(column_index, row_index)]["picked"]
            if row_sum == 5:
                return True

        return False

    @property
    def is_winner(self) -> bool:
        return self._is_winner()

    def _unmarked_sum(self) -> int:
        unmarked_sum = 0
        for row_index in range(0, 5):
            for column_index in range(0, 5):
                if self.board[(column_index, row_index)]["picked"] is False:
                    unmarked_sum += self.board[(column_index, row_index)]["number"]
        return unmarked_sum

    @property
    def unmarked_sum(self) -> int:
        return self._unmarked_sum()

    def pick_number(self, number: int) -> None:
        for row_index in range(0, 5):
            for column_index in range(0, 5):
                if self.board[(column_index, row_index)]["number"] == number:
                    self.board[(column_index, row_index)]["picked"] = True


def run_game(parsed_data: dict) -> dict:
    boards = [Board(item) for item in parsed_data["boards"]]
    for number in parsed_data["numbers"]:
        for board in boards:
            board.pick_number(number)
            if board.is_winner:
                return {"number": number, "unmarked_sum": board.unmarked_sum}
    assert False


def main() -> None:
    data = load_data()
    parsed_data = parse_data(data)
    game_winner = run_game(parsed_data)
    answer = game_winner["number"] * game_winner["unmarked_sum"]
    print(
        f'Answer is {game_winner["number"]} * {game_winner["unmarked_sum"]} = {answer}'
    )


if __name__ == "__main__":
    main()
