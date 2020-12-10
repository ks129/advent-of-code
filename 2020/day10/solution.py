import typing as t


def load_input() -> t.List[int]:
    """Loads input from 'input.txt'."""
    with open('input.txt') as f:
        return list(map(int, f.readlines()))


def part_one(inp: t.List[int]) -> int:
    """
    Solves part 1 of 2020 day 10 puzzle.

    Task is finding multiplication result of 1-jolt and 3-jolt differences.
    """
    inp.sort()

    jolts = [0, 0, 0, 0]

    for j1, j2 in zip([0] + inp, inp + [max(inp) + 3]):
        jolts[j2 - j1] += 1

    return jolts[1] * jolts[3]


def part_two(inp: t.List[int]) -> int:
    """
    Solves part 1 of 2020 day 10 puzzle.

    Task is fining possible ways amount of ordering adapters.
    """
    possibilities = {max(inp) + 3: 1}
    for i in reversed([0] + inp):
        possibilities[i] = sum(possibilities.get(i + k, 0) for k in (1, 2, 3))
    return possibilities[0]


if __name__ == "__main__":
    data = load_input()
    print("2020, Day 10, Part 1 solution:")
    print(part_one(data))
    print("2020, Day 10, Part 2 solution:")
    print(part_two(data))
