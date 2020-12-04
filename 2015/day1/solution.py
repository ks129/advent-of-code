CHARS_MAPPING = {
    "(": 1,
    ")": -1,
}


def load_input() -> str:
    """Load input string from 'input.txt'."""
    with open('input.txt') as f:
        return f.read()


def part_one(inp: str) -> int:
    """
    Solves part 1 of 2015 day 1 puzzle.

    Task is find on what floor santa have to go. `(` means 1 floor up and `(` means 1 floor down.
    """
    return inp.count('(') - inp.count(')')


def part_two(inp: str) -> int:
    """
    Solves part 2 of 2015 day 1 puzzle.

    Task is find at what position is character that commads santa to go to floor -1 (basement).
    """
    floor = 0
    for i, char in enumerate(inp, 1):
        floor += CHARS_MAPPING[char]
        if floor == -1:
            return i


if __name__ == "__main__":
    data = load_input()
    print("2015, Day 1, Part 1 solution:")
    print(part_one(data))
    print("2015, Day 1, Part 2 solution:")
    print(part_two(data))
