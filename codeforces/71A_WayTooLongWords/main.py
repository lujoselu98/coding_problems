import sys


def read_line() -> str:
    return sys.stdin.readline().strip()


def main() -> None:
    n = int(read_line())
    for _ in range(n):
        word = read_line()
        if len(word) > 10:
            print(f"{word[0]}{len(word) - 2}{word[-1]}")
        else:
            print(word)


if __name__ == "__main__":
    main()
