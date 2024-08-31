from typing import Dict, List

BILLION: int = 1_000_000_000


class Moves:
    SPIN: str = "spin"
    EXCHANGE: str = "exchange"
    PARTNER: str = "partner"


class DanceMove:
    def __init__(
        self,
        kind: str,
        spin: int = 0,
        name1: str = "",
        name2: str = "",
        pos1: int = 0,
        pos2: int = 0,
    ) -> None:
        self.kind: str = kind
        self.spin: int = spin
        self.name1: str = name1
        self.name2: str = name2
        self.pos1: int = pos1
        self.pos2: int = pos2


class Dancer:
    def __init__(self, name: str) -> None:
        self.name: str = name


class Dancers:
    def __init__(self, size: int) -> None:
        self.size: int = size
        self.map: Dict[str, Dancer] = {}
        self.order: List[Dancer] = []

        for step in range(size):
            name: str = chr(ord("a") + step)

            dancer: Dancer = Dancer(name)
            self.order.append(dancer)

            self.map[name] = dancer

        self.head: int = 0

    def spin(self, number: int) -> None:
        self.head = (self.head - number) % self.size

    def exchange(self, position1: int, position2: int) -> None:
        # adjust positions
        pos1: int = (self.head + position1) % self.size
        pos2: int = (self.head + position2) % self.size

        # swap dancers
        self.order[pos1], self.order[pos2] = self.order[pos2], self.order[pos1]

    def partner(self, name1: str, name2: str) -> None:
        # swap values
        self.map[name1].name, self.map[name2].name = (
            self.map[name2].name,
            self.map[name1].name,
        )

        # swap pointers
        self.map[name1], self.map[name2] = self.map[name2], self.map[name1]

    def get_dancers(self) -> str:
        output: List[str] = []
        for index in range(self.size):
            output.append(self.order[(self.head + index) % self.size].name)

        return "".join(output)


def parse(filename: str) -> List[DanceMove]:
    with open(filename, "r") as fp:
        data: str = fp.read()

    dance_moves: List[DanceMove] = []

    for move in data.strip().split(","):
        if move.startswith("s"):
            dance_moves.append(DanceMove(Moves.SPIN, spin=int(move[1:])))
        elif move.startswith("x"):
            A, B = move[1:].split("/")
            dance_moves.append(DanceMove(Moves.EXCHANGE, pos1=int(A), pos2=int(B)))
        else:
            A, B = move[1:].split("/")
            dance_moves.append(DanceMove(Moves.PARTNER, name1=A, name2=B))

    return dance_moves


def dance(dancers: Dancers, dance_moves: List[DanceMove]) -> None:

    for dance_move in dance_moves:
        kind: str = dance_move.kind
        match kind:
            case Moves.SPIN:
                dancers.spin(dance_move.spin)
            case Moves.EXCHANGE:
                dancers.exchange(dance_move.pos1, dance_move.pos2)
            case Moves.PARTNER:
                dancers.partner(dance_move.name1, dance_move.name2)


def solution(filename: str, size: int) -> str:
    dance_moves: List[DanceMove] = parse(filename)
    dancers: Dancers = Dancers(size)

    seen: Dict[str, int] = {}

    for index in range(BILLION):
        key: str = dancers.get_dancers()
        if key in seen:
            break
        seen[key] = index
        dance(dancers, dance_moves)

    prefix: int = seen[key]
    cycle: int = index - prefix
    reminding: int = (BILLION - prefix) % cycle

    for index in range(reminding):
        dance(dancers, dance_moves)

    return dancers.get_dancers()


if __name__ == "__main__":
    print(solution("./input.txt", 16))  # "ifocbejpdnklamhg"
