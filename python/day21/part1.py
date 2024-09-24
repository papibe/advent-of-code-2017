import re
from collections import deque
from typing import Deque, Dict, List, Match, Optional, Set, Tuple

Art = List[List[str]]
Rules = Dict[str, str]

INITIAL_ART: Art = [
    [".", "#", "."],
    [".", ".", "#"],
    ["#", "#", "#"],
]

TRANSFORMATIONS: List[str] = [
    "0", "90", "180", "270", "hflip", "90f", "180f", "270f"
]

def parse(filename: str) -> Rules:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    rules: Rules = {}
    for line in data:
        rule, transformation = line.split(" => ")
        rules[rule] = transformation

    # for k, v in rules.items():
    #     print(f"{k = }: {v = }")

    return rules

def rot90(art: Art) -> Art:
    n = len(art)
    rot = [[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rot[i][j] = art[n - j - 1][i]
    return rot

def hflip(tile: Art) -> Art:
    n = len(tile)  # matix size
    flip = [[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            flip[i][j] = tile[n - i - 1][j]
    return flip


def transformation(art, orientation):
    standard = ["0", "90", "180", "270"]
    if orientation in standard:
        for _ in range(standard.index(orientation)):
            art = rot90(art)
        return art

    if orientation == "hflip":
        return hflip(art)

    standardF = ["_", "90f", "180f", "270f"]
    if orientation in standardF:
        art = hflip(art)
        for _ in range(standardF.index(orientation)):
            art = rot90(art)
        return art


def get_transformations(art: Art) -> List[Art]:

    transformations: List[Art] = []
    for trans in TRANSFORMATIONS:
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



def three_enhancement_rule(art: Art, rules: Rules) -> None:
    size: int = len(art)
    n_divitions: int = size // 3

    divisions: List[art] = []
    for index in range(n_divitions):
        division: Art = []
        for row in range(3):
            new_row = []
            for col in range(3):
                new_row.append(art[index * 3 + row][index * 3 + col])
            division.append(new_row)
        divisions.append(division)

    transformations: List[str] = []
    for division in divisions:
        transformed:List[Art] = get_transformations(division)
        for transformation in transformed:
            string_rep: str = stringify(transformation)
            if string_rep in rules:
                transformations.append(rules[string_rep])
                break
            # print_art(transformation)
            # print(string_rep, "\n")
        else:
            raise Exception("wtf")

    for transformation in transformations:
        print(transformation)

    # join pieces
    new_size = (3 + 1) * n_divitions
    art = [[None]*new_size for _ in range(new_size)]
    print(art)
    for index, tranformation in enumerate(transformations):
        print(transformation)
        trans_index: int = 0
        for row in range(3 + 1):
            for col in range(3 + 1):
                print(index * 3 + row, index * 3 + col, trans_index)
                art[index * 3 + row][index * 3 + col] = transformation[trans_index]
                trans_index += 1

            trans_index += 1


    print_art(art)

def two_enhancement_rule(art: Art, rules: Rules) -> None:
    pass


def enhancement_rule(art: Art, rules: Rules, number: int) -> None:
    size: int = len(art)
    n_divitions: int = size // number

    divisions: List[art] = []
    for index in range(n_divitions):
        division: Art = []
        for row in range(number):
            new_row = []
            for col in range(number):
                print(index * number + row, index * number + col)
                new_row.append(art[index * number + row][index * number + col])
            division.append(new_row)
        print("=" * 10)
        divisions.append(division)

    print(divisions)
    print()

    transformations: List[str] = []
    for division in divisions:
        transformed:List[Art] = get_transformations(division)
        for transformation in transformed:
            string_rep: str = stringify(transformation)
            if string_rep in rules:
                transformations.append(rules[string_rep])
                break
            # print_art(transformation)
            # print(string_rep, "\n")
        else:
            raise Exception("wtf")

    for transformation in transformations:
        print(transformation)

    # join pieces
    new_size = (number + 1) * n_divitions
    art = [[" "]*new_size for _ in range(new_size)]
    print(art)
    for index, tranformation in enumerate(transformations):
        print(transformation)
        trans_index: int = 0
        for row in range(number + 1):
            for col in range(number + 1):
                print(index * (number + 1) + row, index * (number + 1) + col, trans_index)
                art[index * (number + 1) + row][index * (number + 1) + col] = transformation[trans_index]
                trans_index += 1
            trans_index += 1
            print_art(art)


    print_art(art)
    print()

    return art




def solve(iterations: int, rules: Rules) -> int:

    art: Art = INITIAL_ART

    for cycle in range(iterations):
        size: int = len(art)

        if size % 2 == 0:
            art = enhancement_rule(art, rules, 2)
        elif size % 3 == 0:
            art = enhancement_rule(art, rules, 3)
        else:
            print("no enhancenment")

        print("end of cycle")
        print_art(art)

    return 0

def solution(filename: str, iterations: int) -> int:
    rules: Rules = parse(filename)
    return solve(iterations, rules)

if __name__ == "__main__":
    print(solution("example.txt", 2))  # 12
    # print(solution("input.txt", 5))  # 0
