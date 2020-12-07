import re
import typing as t
from collections import defaultdict, deque

PARENT_REGEX = re.compile(r"(.+?) bags contain")
CHILD_REGEX = re.compile(r"(\d+) (.+?) bags?[.,]")


def load_input() -> t.Tuple[defaultdict, defaultdict]:
    """Loads input from 'input.txt'."""
    with open('input.txt') as f:
        lines = f.readlines()
    part1 = defaultdict(list)
    part2 = defaultdict(list)
    for line in lines:
        color = PARENT_REGEX.findall(line)[0]
        children = CHILD_REGEX.findall(line)
        for child in children:
            part1[child[1]].append(color)
            part2[color].append(child)
    return part1, part2


def part_one(inp: defaultdict) -> int:
    """
    Solves part 1 of 2020 day 7 puzzle.

    Task is finding how many bags in input can contain at least 1 gold shiny bag.
    """
    result = set()
    color_queue = deque(["shiny gold"])
    while color_queue:
        for value in inp[color_queue.popleft()]:
            if value not in result:
                result.add(value)
                color_queue.append(value)
    return len(result)


def part_two(inp: defaultdict) -> int:
    """
    Solves part 2 of 2020 day 7 puzzle.

    Task is finding how many bags is in gold shiny bag total.
    """
    calculate_inside_bags = lambda color: sum(
        int(child[0]) * (calculate_inside_bags(child[1]) + 1) for child in inp[color]
    )
    return calculate_inside_bags("shiny gold")


if __name__ == "__main__":
    data = load_input()
    print("2020, Day 7, Part 1 solution:")
    print(part_one(data[0]))
    print("2020, Day 7, Part 2 solution:")
    print(part_two(data[1]))
