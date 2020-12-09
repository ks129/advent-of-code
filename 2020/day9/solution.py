import itertools
import typing as t


def load_input() -> t.List[int]:
    """Loads input from 'input.txt'."""
    with open('input.txt') as f:
        return list(map(int, f.readlines()))


def part_one(inp: t.List[int]) -> int:
    """
    Solves part 1 of 2020 day 9 puzzle.

    Task is finding first number in input list that isn't sum of any
    last 25 numbers of input.
    """
    for i in range(len(inp[26:])):
        num = inp[i + 25]
        found = False
        for combo in itertools.combinations(inp[i:i + 25], 2):
            if sum(combo) == num:
                found = True
                break

        if found is False:
            return num


def part_two(inp: t.List[int], broken: int) -> int:
    """
    Solves part 1 of 2020 day 9 puzzle.

    Task is finding number what is wrong and broke program and return it's 25 digit range max + min.
    """
    return [min(r) + max(r) for x in range(len(inp)) for y in range(x, len(inp)) if sum((r := inp[x:y + 1])) == broken][0]


if __name__ == "__main__":
    data = load_input()
    print("2020, Day 9, Part 1 solution:")
    broken_number = part_one(data)
    print(broken_number)
    print("2020, Day 9, Part 2 solution:")
    print(part_two(data, broken_number))
