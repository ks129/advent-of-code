import typing as t


def load_input() -> t.List[str]:
    """Load input from 'input.txt'."""
    with open('input.txt') as f:
        return [line.rstrip("\n") for line in f.readlines()]


def part_one(inp: t.List[str]) -> t.Tuple[int, t.Set[int]]:
    """
    Solves part 1 of 2020 day 5 puzzle.

    Task is finding number locations of plane seats.
    First 7 characters of seat rules show at what row seat is.
    3 last characters show column of seat.
    """
    seats = set()
    for line in inp:
        row = list(range(128))
        col = list(range(8))
        for char in line:
            if char == "R":
                col = col[len(col) // 2:]
            elif char == "L":
                col = col[:len(col) // 2]
            elif char == "B":
                row = row[len(row) // 2:]
            elif char == "F":
                row = row[:len(row) // 2]
        seats.add(row[0] * 8 + col[0])
    return max(seats), seats


def part_two(inp: t.Set[int]) -> int:
    """
    Solves part 2 of 2020 day 5 puzzle.

    Task is finding your own seat.
    """
    ma = max(inp)
    mi = min(inp)
    return list(set(range(mi, ma)) - inp)[0]


if __name__ == "__main__":
    data = load_input()
    print("2020, Day 5, Part 1 solution:")
    part_one_result, new_data = part_one(data)
    print(part_one_result)
    print("2020, Day 5, Part 2 solution:")
    print(part_two(new_data))
