import re
import typing as t

INPUT_REGEX = re.compile(r"(\d+)-(\d+) (\w): (\w+)")


def load_input() -> t.List[t.Tuple[t.Union[int, str]]]:
    """Loads input from 'input.txt' to parsed format."""
    with open('input.txt') as f:
        return INPUT_REGEX.findall(f.read())


def part_one(inp: t.List[t.Tuple[t.Union[int, str]]]) -> int:
    """
    Solves part 1 of 2020 day 2 puzzle.

    Task is find valid passwords from input list.
    Input lines is in format:
        a-b c: d

    a is integer that show how much c-s must be in d.
    b is integer that show max amount of c-s in d.
    c is character (str)
    d is password (str)

    This functions check how much lines follow these rules.
    """
    return sum(1 for a, b, c, d in inp if int(a) <= d.count(c) <= int(b))


def part_two(inp: t.List[t.Tuple[t.Union[int, str]]]) -> int:
    """
    Solves part 2 of 2020 day 2 puzzle.

    Task is finding valid passwords with another rules.
    Input stay same than for part 1, but password is valid when:

    One of positions (a or b) of d is c. Starting index is 1.
    """
    return sum(1 for a, b, c, d in inp if (d[int(a) - 1] == c) ^ (d[int(b) - 1] == c))


if __name__ == "__main__":
    data = load_input()
    print("2020, Day 2, Part 1 result:")
    print(part_one(data))
    print("2020, Day 2, Part 2 result:")
    print(part_two(data))
