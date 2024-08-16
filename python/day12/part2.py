import re
from typing import Dict, List, Match, Optional, Set

AdjacencyList = Dict[int, Set[int]]


def parse(filename: str) -> AdjacencyList:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    regex: str = r"(?P<node>\d+) <-> (?P<node_list>.*)"

    adjacency_list: AdjacencyList = {}

    for line in data:
        matches: Optional[Match[str]] = re.match(regex, line)
        assert matches is not None
        node: int = int(matches.group("node"))
        node_list_str: str = matches.group("node_list")
        adjacency_list[node] = {int(n.strip()) for n in node_list_str.split(",")}

    # just in case: second pass to reflect bidirectional data
    for node, node_list in adjacency_list.items():
        for connected_node in node_list:
            if node not in adjacency_list[connected_node]:
                # print(f"{connected_node} missing {node}")
                adjacency_list[connected_node].add(node)

    return adjacency_list


def solve(pipes: AdjacencyList) -> int:

    parents: List[int] = list(range(len(pipes)))

    def find(p: int) -> int:
        while p != parents[p]:
            p = parents[p]
        return p

    def union(p: int, q: int) -> None:
        root_p, root_q = find(p), find(q)
        parents[root_p] = root_q

    for node, neighbors in pipes.items():
        for neighbor in neighbors:
            union(neighbor, node)

    collection_of_parents: Set[int] = set()
    for node in pipes:
        collection_of_parents.add(find(node))

    return len(collection_of_parents)


def solution(filename: str) -> int:
    pipes: AdjacencyList = parse(filename)
    return solve(pipes)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 2
    print(solution("./input.txt"))  # 209
