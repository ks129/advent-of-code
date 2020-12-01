import typing as t

from itertools import combinations


def load_input() -> t.List[int]:
    """Load input from input.txt file."""
    with open('input.txt') as f:
        return [int(line) for line in f]


def part_one(inp: t.List[int]) -> int:
    """
    Solves part 1 of 2020 day 1 puzzle.

    Task is finding 2 numbers in input list what sum is 2020 and return
    result what you get by multiplying these 2 numbers.
    """
    return [a * b for a, b in combinations(inp, 2) if a + b == 2020][-1]


def part_two(inp: t.List[int]) -> int:
    """
    Solves part 2 of 2020 day 1 puzzle.

    Task is almost same than part 2, only that you have to find 3 numbers
    that sum is 2020 and return result what you get by multiplying
    all these numbers.
    """
    return [a * b * c for a, b, c in combinations(inp, 3) if a + b + c == 2020][-1]


if __name__ == "__main__":
    inp = load_input()
    print("2020, Day 1, Part 1 result:")
    print(part_one(inp))
    print("2020, Day 1, Part 2 result:")
    print(part_two(inp))
