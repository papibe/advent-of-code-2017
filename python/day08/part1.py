import re
from collections import deque
from typing import Dict, List, Optional, Match, Tuple

Instructions = List[List[str]]

class Computer:
    def __init__(self) -> None:
        self.registers: Dict[str, int] = {}

    def add_regisger(self, register: str) -> None:
        self.registers[register] = 0

    def compare(self, register: str, op: str, n: int) -> bool:
        if op == ">":
            return self.registers[register] > n
        if op == "<":
            return self.registers[register] < n
        if op == "<=":
            return self.registers[register] <= n
        if op == ">=":
            return self.registers[register] >= n
        if op == "==":
            return self.registers[register] == n
        if op == "!=":
            return self.registers[register] != n

    def operation(self, register: str, op: str, n: int) -> None:
        if op == "inc":
            self.registers[register] += n
        if op == "dec":
            self.registers[register] -= n

    def get_max_register(self) -> int:
        return max(self.registers.values())


def parse(filename: str) -> Tuple[Computer, Instructions]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    computer: Computer = Computer()
    instructions: Instructions = []

    re_line: str = r"(\w+) (\w+) ([-\d]+) if (\w+) ([!><=]+) ([-\d]+)"
    for line in data:
        matches: Optional[Match] = re.search(re_line, line)
        assert matches is not None
        register1: str = matches.group(1)
        operation: str = matches.group(2)
        number1: str = int(matches.group(3))
        register2: str = matches.group(4)
        comparison: str = matches.group(5)
        number2: str = int(matches.group(6))

        computer.add_regisger(register1)
        computer.add_regisger(register2)

        instructions.append([register1, operation, number1, register2, comparison, number2])

    return computer, instructions


def run_instructions(computer: Computer, instructions: Instructions) -> None:
    for register1, operation, number1, register2, comparison, number2 in instructions:
        if computer.compare(register2, comparison, number2):
            computer.operation(register1, operation, number1)

def solution(filename: str) -> int:
    computer, instructions = parse(filename)
    run_instructions(computer, instructions)
    return computer.get_max_register()


if __name__ == "__main__":
    print(solution("./example.txt"))  # 1
    print(solution("./input.txt"))  # 258
