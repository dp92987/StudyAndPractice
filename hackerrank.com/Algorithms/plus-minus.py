# https://www.hackerrank.com/challenges/plus-minus/problem

# Complete the plusMinus function below.
def plusMinus(arr, n):

    pos = sum(map(lambda x: 1 if x > 0 else 0, arr))
    neg = sum(map(lambda x: 1 if x < 0 else 0, arr))
    zero = sum(map(lambda x: 1 if x == 0 else 0, arr))

    print('{:.6f}'.format(pos/n))
    print('{:.6f}'.format(neg/n))
    print('{:.6f}'.format(zero/n))


def main():
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr, n)


if __name__ == '__main__':
    main()
