import re
from typing import Dict, List, Match, Optional, Set, Tuple

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


def get_unbalance(
    children_weights: Dict[int, List[TreeNode]]
) -> Tuple[int, int, TreeNode]:
    unbalanced_node: TreeNode
    unbalanced_weigth: int
    balanced_weigth: int

    for weight, nodes in children_weights.items():
        if len(nodes) == 1:
            unbalanced_node = nodes[0]
            unbalanced_weigth = weight
        else:
            balanced_weigth = weight

    return balanced_weigth, unbalanced_weigth, unbalanced_node


def balance_weight(node: TreeNode) -> Tuple[bool, int]:
    if not node.children:
        return True, node.weight

    children_weights: Dict[int, List[TreeNode]] = {}
    for child in node.children:
        is_balanced, weight = balance_weight(child)

        if not is_balanced:
            return False, weight

        if weight in children_weights:
            children_weights[weight].append(child)
        else:
            children_weights[weight] = [child]

    if len(children_weights) != 1:
        balanced_weigth, unbalanced_weigth, unbalanced_node = get_unbalance(
            children_weights
        )

        diff_weight: int = balanced_weigth - unbalanced_weigth
        return False, unbalanced_node.weight + diff_weight

    total_children_weight: int = children_weights.popitem()[0]

    return True, node.weight + (len(node.children) * total_children_weight)


def solution(filename: str) -> int:
    root: TreeNode = parse(filename)
    _, weight = balance_weight(root)
    return weight


if __name__ == "__main__":
    print(solution("./example.txt"))  # 60
    print(solution("./input.txt"))  # 256
