import typing as t

DELTAS = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

CLOSE_POSITIONS = lambda x, y: ((dx + x, dy + y) for dx, dy in DELTAS)


def visible_positions(seats: t.Dict[t.Tuple[int, int], str], x: int, y: int) -> t.List[t.Tuple[int, int]]:
    positions = []
    for dx, dy in DELTAS:
        nx = x + dx
        ny = y + dy
        while seats.get((nx, ny)) == ".":
            nx += dx
            ny += dy
        positions.append((nx, ny))
    return positions


def load_input() -> t.List[t.List[str]]:
    """Loads input from 'input.txt'."""
    with open('input.txt') as f:
        return [list(line) for line in f.read().split("\n") if line]


def part_one(inp: t.List[t.List[str]]) -> int:
    """
    Solves part 1 of 2020 day 11 puzzle.

    Task is finding how many seats is occupied when layout don't change anymore.
    """
    seats = {(x, y): inp[y][x] for y in range(len(inp)) for x in range(len(inp[0]))}

    while True:
        new = seats.copy()

        for (x, y), seat in seats.items():
            adj = []
            for close in CLOSE_POSITIONS(x, y):
                adj.append(seats.get(close, "."))

            if seat == "L" and "#" not in adj:
                new[x, y] = "#"
            elif seat == "#" and adj.count("#") >= 4:
                new[x, y] = "L"

        if new == seats:
            return tuple(seats.values()).count("#")

        seats = new


def part_two(inp: t.List[t.List[str]]) -> int:
    """
    Solves part 2 of 2020 day 11 puzzle.

    Almost same than part 1, just you must count seats that users see.
    """
    seats = {(x, y): inp[y][x] for y in range(len(inp)) for x in range(len(inp[0]))}

    while True:
        new = seats.copy()

        for (x, y), seat in seats.items():
            adj = []
            for close in visible_positions(seats, x, y):
                adj.append(seats.get(close, "."))

            if seat == "L" and "#" not in adj:
                new[x, y] = "#"
            elif seat == "#" and adj.count("#") >= 5:
                new[x, y] = "L"

        if seats == new:
            return tuple(seats.values()).count("#")

        seats = new


if __name__ == "__main__":
    data = load_input()
    print("2020, Day 11, Part 1 solution:")
    print(part_one(data))
    print("2020, Day 11, Part 2 solution:")
    print(part_two(data))
