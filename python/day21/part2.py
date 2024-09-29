from copy import deepcopy
from typing import Dict, List

Art = List[List[str]]
Rules = Dict[str, str]

INITIAL_ART: Art = [
    [".", "#", "."],
    [".", ".", "#"],
    ["#", "#", "#"],
]

TRANSFORMATIONS: List[str] = ["0", "90", "180", "270", "hflip", "90f", "180f", "270f"]


def parse(filename: str) -> Rules:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    rules: Rules = {}
    for line in data:
        rule, transformation = line.split(" => ")
        rules[rule] = transformation

    return rules


def rot90(art: Art) -> Art:
    n: int = len(art)
    rot: Art = [[""] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rot[i][j] = art[n - j - 1][i]
    return rot


def hflip(tile: Art) -> Art:
    n: int = len(tile)
    flip: Art = [[""] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            flip[i][j] = tile[n - i - 1][j]
    return flip


def transformation(art: Art, orientation: str) -> Art:
    standard: Dict[str, int] = {"0": 0, "90": 1, "180": 2, "270": 3}
    if orientation in standard:
        for _ in range(standard[orientation]):
            art = rot90(art)
        return art

    if orientation == "hflip":
        return hflip(art)

    standardF: Dict[str, int] = {"_": 0, "90f": 1, "180f": 2, "270f": 3}
    if orientation in standardF:
        art = hflip(art)
        for _ in range(standardF[orientation]):
            art = rot90(art)
        return art

    return art


def get_transformations(art: Art) -> List[Art]:
    transformations: List[Art] = [deepcopy(art)]
    # transformations: List[Art] = []

    for _ in range(len(["90", "180", "270"])):
        art = rot90(art)
        transformations.append(art)

    art = rot90(art)
    art = hflip(art)
    transformations.append(art)

    for _ in range(len(["90f", "180f", "270f"])):
        art = rot90(art)
        transformations.append(art)

    return transformations


def get_transformations__(art: Art) -> List[Art]:
    transformations: List[Art] = []

    for trans in TRANSFORMATIONS:
        # transformations.append(transformation(deepcopy(art), trans))
        transformations.append(transformation(art, trans))

    return transformations


def print_art(art: Art) -> None:
    for row in art:
        print("".join(row))


def stringify(art: Art) -> str:
    output: List[str] = []
    for row in art:
        output.append("".join(row))
    return "/".join(output)


def get_divisions(art: Art, number: int) -> List[Art]:
    size: int = len(art)
    n_divitions: int = size // number
    divisions: List[Art] = []

    for base_row in range(n_divitions):

        for base_col in range(n_divitions):
            start_row: int = base_row * number
            start_col: int = base_col * number

            division: Art = []

            for row in range(start_row, start_row + number):
                new_row: List[str] = []

                for col in range(start_col, start_col + number):
                    new_row.append(art[row][col])
                division.append(new_row)

            divisions.append(division)

    return divisions


cache: Dict[str, str] = {}


def enhancement_rule(art: Art, rules: Rules, number: int) -> Art:

    divisions: List[Art] = get_divisions(art, number)

    transformations: List[str] = []
    for division in divisions:
        key: str = stringify(division)
        if key in cache:
            transformations.append(cache[key])
            continue

        rotations: List[Art] = get_transformations(division)
        for rotation in rotations:
            string_rep: str = stringify(rotation)
            if string_rep in rules:
                transformations.append(rules[string_rep])
                cache[key] = rules[string_rep]
                break
        else:
            raise Exception("not able to find a rule")

    size: int = len(art)
    n_divitions: int = size // number

    # join pieces
    new_size = (number + 1) * n_divitions
    art = [["+"] * new_size for _ in range(new_size)]
    transformation_index: int = 0

    for base_row in range(n_divitions):
        for base_col in range(n_divitions):
            start_row: int = base_row * (number + 1)
            start_col: int = base_col * (number + 1)

            transformation: str = transformations[transformation_index]
            transformation_index += 1
            trans_index: int = 0

            for row in range(start_row, start_row + number + 1):
                for col in range(start_col, start_col + number + 1):
                    art[row][col] = transformation[trans_index]
                    trans_index += 1

                trans_index += 1  # skip "/"

    return art


def count_pixels(art: Art) -> int:
    counter: int = 0

    for row in art:
        for cell in row:
            if cell == "#":
                counter += 1
    return counter


def solve(art: Art, iterations: int, rules: Rules) -> int:

    for cycle in range(iterations):
        # print(cycle)
        size: int = len(art)

        if size % 2 == 0:
            art = enhancement_rule(art, rules, 2)
        elif size % 3 == 0:
            art = enhancement_rule(art, rules, 3)

    return count_pixels(art)


def solution(filename: str, iterations: int) -> int:
    art: Art = INITIAL_ART
    rules: Rules = parse(filename)

    return solve(art, iterations, rules)


if __name__ == "__main__":
    print(solution("input.txt", 18))  # 1984683
