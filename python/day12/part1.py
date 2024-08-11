import re
from collections import deque
from typing import Deque, Dict, List, Match, Optional, Set

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
    connections_to_zero: int = 0

    for node, node_list in pipes.items():
        if node == 0:
            connections_to_zero += 1
            continue

        visited: Set[int] = set()
        queue: Deque[int] = deque([node])
        visited.add(node)

        while queue:
            current: int = queue.popleft()
            if current == 0:
                connections_to_zero += 1
                break

            for neighbor in pipes[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    return connections_to_zero


def solution(filename: str) -> int:
    pipes: AdjacencyList = parse(filename)
    return solve(pipes)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 6
    print(solution("./input.txt"))  # 128
