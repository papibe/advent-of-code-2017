import re
from collections import namedtuple
from typing import List, Match, Optional

Particle = namedtuple("Particle", ["x", "y", "z", "vx", "vy", "vz", "ax", "ay", "az"])


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


def solve(particles: List[Particle], cycles: int, tolerance: int) -> int:
    times: int = 0
    min_particle: int = 0
    previous_min_particle: int = 0

    for _ in range(cycles):
        new_particles: List[Particle] = []
        for index, p in enumerate(particles):
            vx, vy, vz = p.vx + p.ax, p.vy + p.ay, p.vz + p.az
            x, y, z = p.x + vx, p.y + vy, p.z + vz
            new_particles.append(Particle(x, y, z, vx, vy, vz, p.ax, p.ay, p.az))

        particles = new_particles

        # look for this cycle min distance
        min_distance: int = float("inf")  # type: ignore
        for index, p in enumerate(particles):
            distance: int = abs(p.x) + abs(p.y) + abs(p.z)
            if distance < min_distance:
                min_particle = index
                min_distance = distance

        if min_particle == previous_min_particle:
            times += 1
        else:
            times = 0

        if times >= tolerance:
            return min_particle

        previous_min_particle = min_particle

    return min_particle


def solution(filename: str) -> int:
    particles: List[Particle] = parse(filename)
    return solve(particles, cycles=1000, tolerance=300)


if __name__ == "__main__":
    print(solution("./example1.txt"))  # 0
    print(solution("./input.txt"))  # 258
