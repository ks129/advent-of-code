import re
import typing as t

ALL = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

CONSTRAINTS = {
    # Must be 4 digits, in range 1920-2002
    "byr": re.compile(r"19[2-9][0-9]|200[0-2]"),
    # Must be 4 digits, in range 2010-2020
    "iyr": re.compile(r"201[0-9]|2020"),
    # Must be 4 digits, in range 2020-3030
    "eyr": re.compile(r"202[0-9]|2030"),
    # Must be in valid range. Ranges:
    # - cm: 150-193
    # - in: 59-76
    "hgt": re.compile(r"(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in"),
    # Must start with # followed by exactly 6 characters of 0-9 and a-f
    "hcl": re.compile(r"#[0-9a-f]{6}"),
    # Must be item in list
    "ecl": re.compile(r"amb|blu|brn|gry|grn|hzl|oth"),
    # Must be 9 digit number
    "pid": re.compile(r"[0-9]{9}"),
}


def load_input() -> t.List[t.Dict[str, str]]:
    """Load and parse input from 'input.txt'."""
    with open("input.txt") as f:
        raw_passports = [line.rstrip("\n").replace("\n", " ") for line in f.read().split("\n\n")]

    passports = []
    for raw_passport in raw_passports:
        passports.append({item.split(":")[0]: item.split(":")[1] for item in raw_passport.split()})
    return passports


def part_one(inp: t.List[t.Dict[str, str]]) -> t.Tuple[int, t.List[t.Dict[str, str]]]:
    """
    Solves part 1 of 2020 day 4 puzzle.

    Task is to detect amount of valid passports from input.
    Required fields are:
    - byr (Birth Year)
    - iyr (Issue Year)
    - eyr (Expiration Year)
    - hgt (Height)
    - hcl (Hair Color)
    - ecl (Eye Color)
    - pid (Passport ID)
    - cid (Country ID)

    However, when only cid is missing, we can count it valid.
    """
    valid_amount = 0
    valid_passports = []

    for passport in inp:
        # As we don't need to check cid
        passport.pop("cid", None)

        if not ALL - set(passport.keys()):
            valid_amount += 1
            valid_passports.append(passport)

    return valid_amount, valid_passports


def part_two(inp: t.List[t.Dict[str, str]]) -> int:
    """
    Solves part 2 of 2020 day 4 puzzle.

    Task is adding more constraints to passports (part 1 constraints still stay).
    Constraints descriptions is in CONSTRAINTS.
    """
    valid_amount = 0
    for passport in inp:
        checks = {key: bool(constraint.fullmatch(passport[key])) for key, constraint in CONSTRAINTS.items()}
        if all(checks.values()):
            valid_amount += 1
    return valid_amount


if __name__ == "__main__":
    data = load_input()
    print("2020, Day 4, Part 1 result:")
    part_one_valid_amount, valid = part_one(data)
    print(part_one_valid_amount)
    print("2020, Day 4, Part 2 result:")
    print(part_two(valid))
