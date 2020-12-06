import typing as t


def load_input() -> t.List[t.List[str]]:
    """Loads input from 'input.txt'."""
    with open('input.txt') as f:
        return [[c for c in line.strip("\n").split("\n")] for line in f.read().split("\n\n")]


def part_one(inp: t.List[t.List[str]]) -> int:
    """
    Solves part 1 of 2020 day 6 puzzle.

    Task is finding how many "yes"-es is in input total.
    Every unique character in group is one yes.
    """
    return sum(len(set("".join(group))) for group in inp)


def part_two(inp: t.List[t.List[str]]) -> int:
    """
    Solves part 2 of 2020 day 6 puzzle.

    Task is finding how many "yes"-es is answered,
    but this time only counts these answers that all in group
    answered.
    """
    return sum(len(set.intersection(*map(set, group))) for group in inp)


if __name__ == "__main__":
    data = load_input()
    print("2020, Day 6, Part 1 solution:")
    print(part_one(data))
    print("2020, Day 6, Part 2 solution:")
    print(part_two(data))
