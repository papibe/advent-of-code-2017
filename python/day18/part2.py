import asyncio
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

    return program, registers


async def run(
    program_id: int,
    queue_read: asyncio.Queue[int],
    queue_write: asyncio.Queue[int],
    program: List[Instruction],
    registers: Dict[str, int],
) -> int:

    value: int
    pointer: int = 0
    send_times: int = 0
    registers["p"] = program_id
    max_wait: float = 0.0

    while True:
        instr: Instruction = program[pointer]

        match instr.instruction:
            case INSTR.SND:
                if instr.register.isalpha():
                    value = registers[instr.register]
                else:
                    value = int(instr.register)

                send_times += 1
                await queue_write.put(value)

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
                wait: float = 0.001
                while queue_read.qsize() == 0:
                    if wait > 0.002:
                        # print(f"{max_wait = }")
                        return send_times
                    await asyncio.sleep(wait)
                    wait *= 2

                max_wait = max(max_wait, wait)
                value = await queue_read.get()
                registers[instr.register] = value

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

    return 0


async def solve(program: List[Instruction], registers: Dict[str, int]) -> int:
    registers_0: Dict[str, int] = registers.copy()
    registers_1: Dict[str, int] = registers.copy()

    queue_0: asyncio.Queue[int] = asyncio.Queue()  # read for id0 and write for id1
    queue_1: asyncio.Queue[int] = asyncio.Queue()  # write for id0 and read for id1

    program_0 = asyncio.create_task(run(0, queue_0, queue_1, program, registers_0))
    program_1 = asyncio.create_task(run(1, queue_1, queue_0, program, registers_1))

    _: int = await program_0
    send_1: int = await program_1

    return send_1


def solution(filename: str) -> int:
    program, registers = parse(filename)
    return asyncio.run(solve(program, registers))


if __name__ == "__main__":
    print(solution("./example2.txt"))  # 3
    print(solution("./input.txt"))  # 7366
