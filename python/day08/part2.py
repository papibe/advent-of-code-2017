import re
from typing import Callable, Dict, List, Match, Optional, Tuple

Instructions = List[Tuple[str, str, int, str, str, int]]


class Computer:
    def __init__(self) -> None:
        self.registers: Dict[str, int] = {}
        self.max_register_during_process: int = 0

    def add_regisger(self, register: str) -> None:
        self.registers[register] = 0

    def compare(self, register: str, op: str, n: int) -> bool:
        comparison: Dict[str, Callable[[int, int], bool]] = {
            ">": lambda r, n: r > n,
            "<": lambda r, n: r < n,
            "<=": lambda r, n: r <= n,
            ">=": lambda r, n: r >= n,
            "==": lambda r, n: r == n,
            "!=": lambda r, n: r != n,
        }
        return comparison[op](self.registers[register], n)

    def operation(self, register: str, op: str, n: int) -> None:
        operations: Dict[str, Callable[[int, int], int]] = {
            "inc": lambda r, n: r + n,
            "dec": lambda r, n: r - n,
        }
        self.registers[register] = operations[op](self.registers[register], n)

        self.max_register_during_process = max(
            self.max_register_during_process, self.registers[register]
        )

    def get_max_register(self) -> int:
        return max(self.registers.values())


def parse(filename: str) -> Tuple[Computer, Instructions]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    computer: Computer = Computer()
    instructions: Instructions = []

    re_line: str = r"(\w+) (\w+) ([-\d]+) if (\w+) ([!><=]+) ([-\d]+)"
    for line in data:
        matches: Optional[Match[str]] = re.search(re_line, line)
        assert matches is not None
        register1: str = matches.group(1)
        operation: str = matches.group(2)
        number1: int = int(matches.group(3))
        register2: str = matches.group(4)
        comparison: str = matches.group(5)
        number2: int = int(matches.group(6))

        computer.add_regisger(register1)
        computer.add_regisger(register2)

        instructions.append(
            (register1, operation, number1, register2, comparison, number2)
        )

    return computer, instructions


def run_instructions(computer: Computer, instructions: Instructions) -> None:
    for register1, operation, number1, register2, comparison, number2 in instructions:
        if computer.compare(register2, comparison, number2):
            computer.operation(register1, operation, number1)


def solution(filename: str) -> int:
    computer, instructions = parse(filename)
    run_instructions(computer, instructions)
    return computer.max_register_during_process


if __name__ == "__main__":
    print(solution("./example.txt"))  # 10
    print(solution("./input.txt"))  # 5035
