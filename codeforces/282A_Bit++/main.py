import sys


def read_line():
    return sys.stdin.readline().strip()


def main():
    n = int(read_line())
    x = 0
    for i in range(n):
        s = read_line()
        if "++" in s:
            x += 1
        else:
            x -= 1
    print(x)


if __name__ == "__main__":
    main()
