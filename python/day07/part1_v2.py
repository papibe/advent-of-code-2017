import re
from typing import Dict, List, Match, Optional, Set

Programs = Dict[str, List[str]]


class TreeNode:
    def __init__(self, name: str, weight: int) -> None:
        self.name: str = name
        self.weight: int = weight
        self.children: List[TreeNode] = []

    def add_child(self, node: "TreeNode") -> None:
        self.children.append(node)


def parse(filename: str) -> TreeNode:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    programs: Dict[str, TreeNode] = {}

    regex: str = r"^(\w+) \((\d+)\)"
    matches: Optional[Match[str]]

    # first pass build main nodes
    for line in data:
        matches = re.search(regex, line)
        assert matches is not None
        name: str = matches.group(1)
        weight: int = int(matches.group(2))
        programs[name] = TreeNode(name, weight)

    candidates_for_root: Set[str] = set(list(programs.keys()))

    # second pass add child nodes
    for line in data:
        if "->" not in line:
            continue

        matches = re.search(regex, line)
        assert matches is not None
        main_name: str = matches.group(1)

        upper_programs: List[str] = line.split(" -> ")[1].split(", ")
        for upper_program in upper_programs:
            programs[main_name].add_child(programs[upper_program])
            candidates_for_root.remove(upper_program)

    assert len(candidates_for_root) == 1

    return programs[candidates_for_root.pop()]


def solution(filename: str) -> str:
    root: TreeNode = parse(filename)
    return root.name


if __name__ == "__main__":
    print(solution("./example.txt"))  # "tknk"
    print(solution("./input.txt"))  # bpvhwhh
