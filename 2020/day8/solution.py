import operator
import re
import typing as t

OPERATORS = {
    "+": operator.add,
    "-": operator.sub
}

OPPOSITE = {
    "jmp": "nop",
    "nop": "jmp"
}

INPUT_REGEX = re.compile(r"(acc|jmp|nop) ([+-])(\d+)")


def load_input() -> t.List[t.Tuple[str, str, int]]:
    """Loads input from 'input.txt'."""
    with open('input.txt') as f:
        return [(line[0], line[1], int(line[2])) for line in INPUT_REGEX.findall(f.read())]


def run(inp: t.List[t.Tuple[str, str, int]]) -> t.Tuple[int, bool]:
    """Runs solver 'core'. Returns result and does this finished successfully (didn't repeat)."""
    position = 0
    accumulator = 0
    success = True
    ran = []
    while True:
        if position in ran:
            success = False
            break
        elif position > len(inp) - 1:
            break

        ran.append(position)

        if inp[position][0] == "acc":
            accumulator = OPERATORS[inp[position][1]](accumulator, inp[position][2])
            position += 1
        elif inp[position][0] == "jmp":
            position = OPERATORS[inp[position][1]](position, inp[position][2])
        else:
            position += 1

    return accumulator, success


def part_one(inp: t.List[t.Tuple[str, str, int]]) -> int:
    """
    Solves part 1 of 2020 day 8 puzzle.

    Task is returning result that accumulator have when first position repeats time.
    """
    return run(inp)[0]


def part_two(inp: t.List[t.Tuple[str, str, int]]) -> int:
    """
    Solves part 2 of 2020 day 8 puzzle.

    Task is returning result after finding corrupted action that didn't let program finish.
    """
    for i, line in enumerate(inp):
        if line[0] in OPPOSITE:
            new_input = inp.copy()
            new_input[i] = (OPPOSITE[line[0]], line[1], line[2])
            score, success = run(new_input)
            if success:
                return score


if __name__ == "__main__":
    data = load_input()
    print("2020, Day 8, Part 1 solution:")
    print(part_one(data))
    print("2020, Day 8, Part 2 solution:")
    print(part_two(data))
