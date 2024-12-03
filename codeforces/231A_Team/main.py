import sys


def read_line():
    return sys.stdin.readline().strip()


def main():
    n = int(read_line())
    count = 0
    for _ in range(n):
        a, b, c = map(int, read_line().split())
        if a + b + c >= 2:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
