import math
import typing as t


def load_input() -> t.List[t.List[str]]:
    """Loads input from 'input.txt'."""
    with open("input.txt") as f:
        return [list(line.strip("\n") * 3000) for line in f]


def part_one(inp: t.List[t.List[str]], movement: t.Tuple[int, int] = (3, 1)) -> int:
    """
    Solves part 1 of 2020 day 3 puzzle.

    Task is finding how much trees is in road when moving with such step:
    1 tile below and 3 right. Input map will repeat.
    """
    trees = 0
    height = len(inp)
    width = len(inp[0])
    for i, row in enumerate(range(0, height, movement[1])):
        column = (movement[0] * i) % width
        trees += int(inp[row][column] == "#")

    return trees


def part_two(inp: t.List[t.List[str]]) -> int:
    """
    Solves part 2 of 2020 day 3 puzzle.

    Task is finding sum of trees when using different slopes:
    - Right 1, down 1
    - Right 3, down 1
    - Right 5, down 1
    - Right 7, down 1
    - Right 1, down 2
    """
    return math.prod(part_one(inp, slope) for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])


if __name__ == "__main__":
    data = load_input()
    print("2020, Day 3, Part 1 result:")
    print(part_one(data))
    print("2020, Day 3, Part 2 result:")
    print(part_two(data))
