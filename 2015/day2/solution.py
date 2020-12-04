import typing as t


def load_input() -> t.List[t.Tuple[int]]:
    """Load puzzle input in 'input.txt'."""
    with open('input.txt') as f:
        return [tuple(map(int, line.split("x"))) for line in f.readlines()]


def part_one(inp: t.List[t.Tuple[int]]) -> int:
    """
    Solves part 1 of 2015 day 2 puzzle.

    Task is calculating amount of wrapping paper. Input is list of package sizes.
    Formula: 2*l*w + 2*w*h + 2*h*l + smallest side extra.
    """
    return sum((2 * l * w) + (2 * w * h) + (2 * h * l) + min((l * w, w * h, h * l)) for l, w, h in inp)


def part_two(inp: t.List[t.Tuple[int]]) -> int:
    """
    Solves part 2 of 2015 day 2 puzzle.

    Task is calculating ribbon amount required.
    Formula: (l + l + w + w) + (l * w * h)
    """
    return sum(2 * min(l + w, w + h, h + l) + (l * w * h) for l, w, h in inp)


if __name__ == "__main__":
    data = load_input()
    print("2015, Day 2, Part 1 solution:")
    print(part_one(data))
    print("2015, Day 2, Part 2 solution:")
    print(part_two(data))
