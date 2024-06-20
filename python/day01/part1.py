def parse(filename: str) -> str:
    with open(filename, "r") as fp:
        return fp.read().splitlines()[0]


def solve(data: str) -> int:
    n: int = len(data)
    total_sum: int = 0

    for index in range(n):
        if data[index] == data[(index + 1) % n]:
            total_sum += int(data[index])

    return total_sum


def solution(filename: str) -> int:
    data: str = parse(filename)
    return solve(data)


if __name__ == "__main__":
    print(solution("./input.txt"))  # 1141
