def main():
    restaurants = {1, 2, 3, 4, 5}
    a, b, c, d = map(int, input().split())
    print((restaurants - {a, b, c, d}).pop())


if __name__ == "__main__":
    main()
