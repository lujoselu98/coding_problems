import sys


def read_input() -> int:
    return int(sys.stdin.readline().strip())


def main(w: int) -> str:
    if w % 2 == 0 and w > 2:
        return "YES"
    return "NO"


if __name__ == "__main__":
    print(main(read_input()))
