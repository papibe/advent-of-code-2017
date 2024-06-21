def parse(filename: str) -> str:
    with open(filename, "r") as fp:
        return fp.read().splitlines()[0]


def solve(data: str) -> int:
    n: int = len(data)
    half_distance: int = n // 2
    total_sum: int = 0

    for index in range(n):
        if data[index] == data[(index + half_distance) % n]:
            total_sum += int(data[index])

    return total_sum


def solution(filename: str) -> int:
    data: str = parse(filename)
    return solve(data)


if __name__ == "__main__":
    print(solution("./input.txt"))  # 950
