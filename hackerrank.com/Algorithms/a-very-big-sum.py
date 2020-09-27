# https://www.hackerrank.com/challenges/a-very-big-sum/problem

import os


# Complete the a_very_big_sum function below.
def a_very_big_sum(ar):
    return sum(ar)


def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    _ = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = a_very_big_sum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()


if __name__ == '__main__':
    main()
