from collections import namedtuple
from typing import Dict, List, Tuple

# type definitions
Instruction = namedtuple("Instruction", ["instruction", "register", "param"])
Registers = Dict[str, int]


class INSTR:
    SND: str = "snd"
    SET: str = "set"
    ADD: str = "add"
    MUL: str = "mul"
    MOD: str = "mod"
    RCV: str = "rcv"
    JGZ: str = "jgz"


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
    for ins in program:
        if ins.register.isalpha():
            registers[ins.register] = 0
        if ins.param.isalpha():
            registers[ins.register] = 0

    # add sound register
    registers["snd"] = 0

    return program, registers


def run(program: List[Instruction], registers: Dict[str, int]) -> int:
    pointer: int = 0
    value: int

    while True:
        instr: Instruction = program[pointer]

        match instr.instruction:
            case INSTR.SND:
                registers["snd"] = registers[instr.register]

            case INSTR.SET:
                if instr.param.isalpha():
                    value = registers[instr.param]
                else:
                    value = int(instr.param)
                registers[instr.register] = value

            case INSTR.ADD:
                if instr.param.isalpha():
                    value = registers[instr.param]
                else:
                    value = int(instr.param)
                registers[instr.register] += value

            case INSTR.MUL:
                if instr.param.isalpha():
                    value = registers[instr.param]
                else:
                    value = int(instr.param)
                registers[instr.register] *= value

            case INSTR.MOD:
                if instr.param.isalpha():
                    value = registers[instr.param]
                else:
                    value = int(instr.param)
                registers[instr.register] %= value

            case INSTR.RCV:
                if instr.register.isalpha():
                    value = registers[instr.register]
                else:
                    value = int(instr.register)
                if value != 0:
                    break

            case INSTR.JGZ:
                x: int
                if instr.register.isalpha():
                    x = registers[instr.register]
                else:
                    x = int(instr.register)

                if instr.param.isalpha():
                    value = registers[instr.param]
                else:
                    value = int(instr.param)

                if x > 0:
                    pointer += value
                    continue

        pointer += 1

    return registers["snd"]


def solution(filename: str) -> int:
    program, registers = parse(filename)
    return run(program, registers)


if __name__ == "__main__":
    print(solution("./example1.txt"))  # 4
    print(solution("./input.txt"))  # 2951
