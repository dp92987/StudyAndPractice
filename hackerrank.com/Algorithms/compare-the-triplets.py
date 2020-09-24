# https://www.hackerrank.com/challenges/compare-the-triplets/problem
import os


# Complete the compareTriplets function below.
def compare_triplets(x, y):
    rx = ry = 0
    for z in zip(x, y):
        if z[0] - z[1] > 0:
            rx += 1
        elif z[0] - z[1] < 0:
            ry += 1
    return [rx, ry]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compare_triplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
