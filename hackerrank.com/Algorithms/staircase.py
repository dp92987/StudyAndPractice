# https://www.hackerrank.com/challenges/staircase/problem


# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        print(f'{" "*(n-i-1)}{"#"*(i+1)}')


def main():
    n = int(input())

    staircase(n)


if __name__ == '__main__':
    main()
