from typing import Dict, List, Set


class Component:
    def __init__(self, port1: int, port2: int) -> None:
        self.port1: int = port1
        self.port2: int = port2
        self.used1: bool = False
        self.used2: bool = False

    def get_value(self) -> int:
        return self.port1 + self.port2

    def __repr__(self) -> str:
        return f"{self.port1},{self.port2}"


def parse(filename: str) -> List[Component]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    components: List[Component] = []

    for line in data:
        ports: List[str] = line.split("/")
        port1, port2 = int(ports[0]), int(ports[1])
        components.append(Component(port1, port2))

    return components


def get_bridge_strength(bridge: List[Component]) -> int:
    strength: int = 0
    for component in bridge:
        strength += component.get_value()

    return strength


def solve(bridge: List[Component], top: int, cmap: Dict[int, Set[Component]]) -> int:
    if not cmap or top not in cmap or not cmap[top]:
        return get_bridge_strength(bridge)

    strengths: List[int] = []
    matching_components: List[Component] = list(cmap[top])

    # add next component
    for component in matching_components:
        bridge.append(component)
        ntop: int = component.port1 if top == component.port2 else component.port2
        cmap[top].remove(component)
        if top != ntop:
            cmap[ntop].remove(component)

        strengths.append(solve(bridge, ntop, cmap))

        # backtrack
        bridge.pop()
        cmap[top].add(component)
        cmap[ntop].add(component)

    return max(strengths)


def solution(filename: str) -> int:
    components: List[Component] = parse(filename)

    # create a fast way to get to the next component
    cmap: Dict[int, Set[Component]] = {}
    for component in components:
        if component.port1 not in cmap:
            cmap[component.port1] = set()
        cmap[component.port1].add(component)

        if component.port2 not in cmap:
            cmap[component.port2] = set()
        cmap[component.port2].add(component)

    pit: Component = Component(0, 0)
    bridge: List[Component] = [pit]
    bridge_top: int = 0

    return solve(bridge, bridge_top, cmap)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 31
    print(solution("./input.txt"))  # 1940
