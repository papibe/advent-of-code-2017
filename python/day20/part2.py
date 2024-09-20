import re
from collections import namedtuple
from typing import Dict, List, Match, Optional

Particle = namedtuple("Particle", ["x", "y", "z", "vx", "vy", "vz", "ax", "ay", "az"])
Position = namedtuple("Position", ["x", "y", "z"])


def parse(filename: str) -> List[Particle]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    regex: str = (
        r"p=<([-+]?\d+),([-+]?\d+),([-+]?\d+)>, v=<([-+]?\d+),([-+]?\d+),([-+]?\d+)>, a=<([-+]?\d+),([-+]?\d+),([-+]?\d+)>"
    )
    particles: List[Particle] = []

    for line in data:
        match: Optional[Match[str]] = re.match(regex, line)
        assert match is not None

        # position
        x: int = int(match.group(1))
        y: int = int(match.group(2))
        z: int = int(match.group(3))
        # velocity
        vx: int = int(match.group(4))
        vy: int = int(match.group(5))
        vz: int = int(match.group(6))
        # acceleration
        ax: int = int(match.group(7))
        ay: int = int(match.group(8))
        az: int = int(match.group(9))

        particles.append(Particle(x, y, z, vx, vy, vz, ax, ay, az))

    return particles


def solve(particles: List[Particle], cycles: int) -> int:

    for _ in range(cycles):
        current_positions: Dict[Position, List[Particle]] = {}
        for index, p in enumerate(particles):
            vx, vy, vz = p.vx + p.ax, p.vy + p.ay, p.vz + p.az
            x, y, z = p.x + vx, p.y + vy, p.z + vz

            position: Position = Position(x, y, z)
            particle: Particle = Particle(x, y, z, vx, vy, vz, p.ax, p.ay, p.az)

            if position in current_positions:
                current_positions[position].append(particle)
            else:
                current_positions[position] = [particle]

        particles = []
        for k, v in current_positions.items():
            if len(v) == 1:
                particles.append(v[0])

    return len(current_positions)


def solution(filename: str) -> int:
    particles: List[Particle] = parse(filename)
    return solve(particles, cycles=1000)


if __name__ == "__main__":
    print(solution("./example2.txt"))  # 1
    print(solution("./input.txt"))  # 707
