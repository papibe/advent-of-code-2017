import re
from dataclasses import dataclass
from typing import Dict, List, Match, Optional, Set, Tuple

LAST: int = -1


@dataclass
class Rule:
    write: int
    movement: int
    next_state: str


class State:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.rules: Dict[int, Rule] = {}

    def add_rule(self, value: int, write: int, movement: str, next_state: str) -> None:
        self.rules[value] = Rule(
            write=write,
            movement=1 if movement == "right" else -1,
            next_state=next_state,
        )

    def get_write_value(self, value: int) -> int:
        return self.rules[value].write

    def get_movement(self, value: int) -> int:
        return self.rules[value].movement

    def get_next_state(self, value: int) -> str:
        return self.rules[value].next_state


class Tape:
    def __init__(self) -> None:
        self.tape: Set[int] = set()

    def get_value(self, position: int) -> int:
        if position in self.tape:
            return 1
        return 0

    def set_value(self, position: int, value: int) -> None:
        if value == 0 and position in self.tape:
            self.tape.remove(position)
            return

        if value == 0 and position not in self.tape:
            return

        self.tape.add(position)

    def len(self) -> int:
        return len(self.tape)


def parse(filename: str) -> Tuple[str, int, Dict[str, State]]:
    with open(filename, "r") as fp:
        data: str = fp.read()

    blocks: List[str] = data.split("\n\n")

    header_re: str = (
        r"Begin in state (\w).\nPerform a diagnostic checksum after (\d+) steps."
    )
    match: Optional[Match[str]] = re.match(header_re, blocks[0])
    assert match is not None

    initial_state: str = match.group(1)
    steps: int = int(match.group(2))

    # parse states:
    block_re: str = r"""In state (\w):
  If the current value is (\d):
    - Write the value (\d).
    - Move one slot to the (\w+).
    - Continue with state (\w).
  If the current value is (\d):
    - Write the value (\d).
    - Move one slot to the (\w+).
    - Continue with state (\w)."""

    states: Dict[str, State] = {}

    for block in blocks[1:]:
        match = re.match(block_re, block)
        assert match is not None

        state_name: str = match.group(1)
        state: State = State(state_name)

        # first rule
        current_value: int = int(match.group(2))
        write_value: int = int(match.group(3))
        movement: str = match.group(4)
        next_state: str = match.group(5)
        state.add_rule(current_value, write_value, movement, next_state)

        # second rule
        current_value = int(match.group(6))
        write_value = int(match.group(7))
        movement = match.group(8)
        next_state = match.group(9)
        state.add_rule(current_value, write_value, movement, next_state)

        states[state_name] = state

    return initial_state, steps, states


def solve(initial_state: str, steps: int, states: Dict[str, State], tape: Tape) -> int:
    current_position: int = 0
    current_state: str = initial_state

    for counter in range(steps):
        state: State = states[current_state]

        current_value: int = tape.get_value(current_position)
        write_value: int = state.get_write_value(current_value)
        tape.set_value(current_position, write_value)

        current_position += state.get_movement(current_value)
        current_state = state.get_next_state(current_value)

    return tape.len()


def solution(filename: str) -> int:
    initial_state, steps, states = parse(filename)
    tape: Tape = Tape()
    return solve(initial_state, steps, states, tape)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 3
    print(solution("./input.txt"))  # 633
