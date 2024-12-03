import sys


def main():
    _ = int(sys.stdin.readline().strip())
    numbers = list(map(int, sys.stdin.readline().strip().split()))

    odd_count, even_count = 0, 0
    odd_index, even_index = 0, 0

    for i, num in enumerate(numbers):
        if num % 2 == 0:
            even_count += 1
            even_index = i + 1
        else:
            odd_count += 1
            odd_index = i + 1

        if odd_count > 1 and even_count == 1:
            print(even_index)
            break
        if even_count > 1 and odd_count == 1:
            print(odd_index)
            break


if __name__ == "__main__":
    main()
