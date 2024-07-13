import re
from typing import Dict, List, Match, Optional, Set

Programs = Dict[str, List[str]]


def parse(filename: str) -> Programs:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    programs: Dict[str, List[str]] = {}

    regex: str = r"^(\w+) \((\d+)\)"
    for line in data:
        matches: Optional[Match[str]] = re.search(regex, line)
        assert matches is not None
        program: str = matches.group(1)
        # weigth: int = int(matches.group(2))

        if "->" in line:
            upper_programs: List[str] = line.split(" -> ")[1].split(", ")
            programs[program] = upper_programs
        else:
            programs[program] = []

    return programs


def solution(filename: str) -> str:
    programs: Programs = parse(filename)
    programs_with_parents: Set[str] = set()

    for _, upper_programs in programs.items():
        programs_with_parents |= set(upper_programs)

    programs_with_no_parent: Set[str] = (
        set(list(programs.keys())) - programs_with_parents
    )
    assert len(programs_with_no_parent) == 1

    return programs_with_no_parent.pop()


if __name__ == "__main__":
    print(solution("./example.txt"))  # "tknk"
    print(solution("./input.txt"))  # bpvhwhh
