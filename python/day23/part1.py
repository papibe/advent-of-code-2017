from collections import namedtuple
from typing import Dict, List, Tuple

# type definitions
Instruction = namedtuple("Instruction", ["instruction", "register", "param"])
Registers = Dict[str, int]


class INSTR:
    SET: str = "set"
    MUL: str = "mul"
    SUB: str = "sub"
    JNZ: str = "jnz"


def parse(filename: str) -> Tuple[List[Instruction], Registers]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    # parse program
    program: List[Instruction] = []
    for line in data:
        parsed: List[str] = line.split()
        instuction: Instruction = Instruction(
            instruction=parsed[0],
            register=parsed[1],
            param=parsed[2] if len(parsed) == 3 else "",
        )
        program.append(instuction)

    # create registers
    registers: Dict[str, int] = {}
    for register in "abcdefgh":
        registers[register] = 0

    return program, registers


def run(program: List[Instruction], registers: Registers) -> int:
    value: int
    pointer: int = 0
    mul_times: int = 0

    while 0 <= pointer < len(program):
        instr: Instruction = program[pointer]

        match instr.instruction:

            case INSTR.SET:
                if instr.param.isalpha():
                    value = registers[instr.param]
                else:
                    value = int(instr.param)
                registers[instr.register] = value

            case INSTR.MUL:
                mul_times += 1
                if instr.param.isalpha():
                    value = registers[instr.param]
                else:
                    value = int(instr.param)
                registers[instr.register] *= value

            case INSTR.SUB:
                if instr.param.isalpha():
                    value = registers[instr.param]
                else:
                    value = int(instr.param)
                registers[instr.register] -= value

            case INSTR.JNZ:
                x: int
                if instr.register.isalpha():
                    x = registers[instr.register]
                else:
                    x = int(instr.register)

                if instr.param.isalpha():
                    value = registers[instr.param]
                else:
                    value = int(instr.param)

                if x != 0:
                    pointer += value
                    continue

            case _:
                raise Exception("Unknown instruction")

        pointer += 1

    return mul_times


def solution(filename: str) -> int:
    program, registers = parse(filename)
    return run(program, registers)


if __name__ == "__main__":
    print(solution("./input.txt"))  # 6724
